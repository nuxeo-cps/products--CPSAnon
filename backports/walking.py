from Acquisition import aq_base
from Globals import InitializeClass
from AccessControl import ClassSecurityInfo
from Products.CPSCore.CPSBase import CPSBaseBTreeFolder
from Products.CPSCore import ProxyBase
from Products.CPSCore.ProxyBase import ProxyDocument
from Products.CPSCore.ProxyBase import ProxyFolder
from Products.CPSCore.ProxyBase import ProxyBTreeFolder
from Products.CPSCore.ProxyBase import ProxyFolderishDocument
from Products.CPSCore.ProxyBase import ProxyBTreeFolderishDocument

security = ClassSecurityInfo()
CPSBaseBTreeFolder.security = security

security.declarePrivate('iterValues')
def iterValues(self, meta_types=None):
    """like objectValues, but a proper generator.
    TODO: also make iterIds and iterItems."""
    if meta_types is None:
        for o in self._tree.itervalues():
            yield o.__of__(self)
        return

    for mt in meta_types:
        ids = self._mt_index.get(mt)
        if ids is None:
            continue
        for oid in ids.iterkeys():
            o = self._getOb(oid, default=None)
            if o is not None:
                yield o
            else:
                logger.warn("Inconsistent id %r in %s, found in "
                            "meta_types indexes, but could not fetch",
                            oid, self)
CPSBaseBTreeFolder.iterValues = iterValues
InitializeClass(CPSBaseBTreeFolder)

def walk(base, meta_types=()):
    """Generator that walks the object hierarchy top-down.

    If you use it in a loop, you must take care of not changing the relevant
    part of hierarchy within that loop.
    """
    it = getattr(aq_base(base), 'iterValues', None)
    if it is None:
        it = base.objectValues
    else:
        it = base.iterValues # the previous has no aq

    for ob in it(meta_types):
        yield ob
        for subob in walk(ob, meta_types=meta_types):
            yield subob

def walk_cps_folders(base):
    """Generator to walk the cps folders."""
    for o in walk(base, meta_types=(ProxyFolder.meta_type,
                                    ProxyBTreeFolder.meta_type)):
        yield o
ProxyBase.walk_cps_folders = walk_cps_folders

def walk_cps_folderish(base):
    """Generator to walk the cps folders and folderish documents"""
    for o in walk(base, meta_types=(ProxyFolder.meta_type,
                                    ProxyBTreeFolder.meta_type,
                                    ProxyFolderishDocument.meta_type,
                                    ProxyBTreeFolderishDocument.meta_type)):
        yield o
ProxyBase.walk_cps_folderish = walk_cps_folderish

def walk_cps_proxies(base):
    """Generator to walk all proxies below."""

    for o in walk(base, meta_types=(ProxyDocument.meta_type,
                                    ProxyFolder.meta_type,
                                    ProxyBTreeFolder.meta_type,
                                    ProxyFolderishDocument.meta_type,
                                    ProxyBTreeFolderishDocument.meta_type)):
        yield o
ProxyBase.walk_cps_proxies = walk_cps_proxies

def walk_cps_except_folders(base):
    """Generator to walk all proxies below except folders.

    Useful mostly within loops already going through all folders."""

    for o in walk(base, meta_types=(ProxyDocument.meta_type,
                                    ProxyFolderishDocument.meta_type,
                                    ProxyBTreeFolderishDocument.meta_type)):
        yield o
ProxyBase.walk_cps_except_folders = walk_cps_except_folders
