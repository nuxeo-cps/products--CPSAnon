from Products.CPSAnon.hacks.exclude4zexp import export_file
from Products.CPSAnon.backports import cpsjob

def save_excluded(exclf, oids):
    efh = open(exclf, 'wb')
    # oid length has probably never changed in the history of ZODB, but why
    # harcode it ?
    efh.write('%02d' % len(oids[0]))
    efh.write(''.join(oids))
    efh.close()

def dump(portal, outf, exclf):
    excl_rpaths = ['portal_repository', 'workspaces', 'sections',
                   'portal_catalog:_catalog',
                   'members', 'portal_proxies']

    excl_rpaths.extend(['portal_trees/%s:_infos' % tid
                        for tid in portal.portal_trees.objectIds()])

    # TODO relations, etc ?
    oids = export_file(portal, '', outf, excluded=excl_rpaths)
    save_excluded(exclf, oids)

if __name__ == '__main__':
    optparser = cpsjob.optparser
    portal, options, args = cpsjob.bootstrap(app)
    if len(args) != 2:
        optparser.error("Please provide two job arguments : "
                        "output file and exclusion file")

    dump(portal, *args)
