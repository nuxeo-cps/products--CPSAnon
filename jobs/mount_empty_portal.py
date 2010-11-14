import transaction
from AccessControl.SecurityManagement import newSecurityManager
from Products.ZCatalog.Catalog import Catalog
from Products.CPSCore.utils import bhasattr
from Products.CPSCore.ProxyTool import ProxyTool
from Products.CPSCore.ObjectRepositoryTool import ObjectRepositoryTool
from Products.CPSAnon.hacks.exclude4zexp import import_file
from Products.CPSAnon.backports import cpsjob

def login(app, user_id):
    aclu = app.acl_users
    try:
        user = aclu.getUser(user_id).__of__(aclu)
    except KeyError:
        logger.fatal("Please run this as a registered toplevel Zope user.")
        sys.exit(1)

    if not user.has_role('Manager'):
        logger.error("The user %s doesn't have the Manager role", user_id)
        sys.exit(1)

    newSecurityManager(None, user)

def read_exclusion_file(exclf):
    """Read the excluded oids in format made by dump_empty_portal"""
    f = open(exclf)
    l = int(f.read(2)) # oid length
    oids = []
    while True:
        oid = f.read(l)
        if not oid:
            f.close()
            return oids
        oids.append(oid)

class PortalMounter(object):

    def __init__(self, app, portal_id):
        self.app = app
        self.portal_id = portal_id

    def createTools(self, *classes):
        for ToolClass in classes:
            tool = ToolClass()
            tid = tool.getId()
            if bhasattr(self.portal, tid):
                logger.warn(
                    "Tool %s already present, not reconstructing." % tid)
                continue
            self.portal._setObject(tid, tool)

    def fixupCatalog(self):
        cat = self.portal.portal_catalog
        if cat.meta_type == 'CMF Catalog' and not bhasattr(cat, '_catalog'):
            cat._catalog = Catalog()

    def fixupTrees(self):
        for tree in self.portal.portal_trees.objectValues(['CPS Tree Cache']):
            tree._clear()

    def fixup(self):
        """Recreates empty objects that aren't in the export.

        No support for content roots (workspaces, sections) yet. Might be
        installation-dependent anyway
        """
        self.createTools(ProxyTool, ObjectRepositoryTool)
        self.fixupCatalog()
        self.fixupTrees()

    def loadPortal(self):
        self.portal = self.app[self.portal_id]

    def beforeImport(self):
        self.deactivateCatalogs()

    def afterImport(self):
        self.reactivateCatalogs()

    def deactivateCatalogs(self):
        from Products.ZCatalog.ZCatalog import ZCatalog
        self._save_catalog_object = ZCatalog.catalog_object
        def catalog_object(*args, **kwargs):
            return
        ZCatalog.catalog_object = catalog_object

    def reactivateCatalogs(self):
        from Products.ZCatalog.ZCatalog import ZCatalog
        ZCatalog.catalog_object = self._save_catalog_object

    def mount(self, zexp, exclf):
        """Mount the CPS portal from zexp, with excluded OIDs as in exclf."""

        self.beforeImport()
        import_file(self.app, zexp, read_exclusion_file(exclf))
        self.afterImport()
        transaction.commit()
        self.loadPortal()
        self.fixup()
        transaction.commit()

def main(app):
    optparser = cpsjob.optparser
    options, args = optparser.parse_args()

    kw = options.__dict__
    login(app, kw.pop('user_id'))
    app = cpsjob.makerequest(app)

    if len(args) != 3:
        optparser.error("Please provide three arguments : "
                        "portal id, input file and exclusion file")

    mounter = PortalMounter(app, args[0])
    mounter.mount(*args[1:])


if __name__ == '__main__':
    main(app)
