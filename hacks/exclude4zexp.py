"""This patch brings selected object exclusion to import/export of ZODB.

the exportFile function gets a new kwarg : excluded_oids
the result can be imported *only if* the same oids are
specified to the importFile function.

This should work for lots of different Zope versions :
the only difference of ZODB.ExportImport between Zope 2.8.3, Zope 2.9.12 and
Zope 2.10.12 is a comment saying it's getting old.
"""
from cStringIO import StringIO
from cPickle import Pickler, Unpickler
from tempfile import TemporaryFile
import logging

from ZODB.POSException import ExportError
from ZODB.utils import p64, u64
from ZODB.serialize import referencesf
from ZODB.ExportImport import ExportImport
from ZODB.ExportImport import export_end_marker, Ghost, persistent_id

def exportFile(self, oid, f=None, excluded_oids=('\x00\x00\x00\x00\x00\x00+\x9e',)):
    if f is None:
        f = TemporaryFile()
    elif isinstance(f, str):
        f = open(f,'w+b')
    f.write('ZEXP')
    oids = [oid]
    done_oids = {}
    done=done_oids.has_key
    load=self._storage.load
    while oids:
        oid = oids.pop(0)
        # GR patch is just the line below
        if oid in done_oids or oid in excluded_oids:
            continue
        done_oids[oid] = True
        try:
            p, serial = load(oid, self._version)
        except:
            logger.debug("broken reference for oid %s", repr(oid),
                         exc_info=True)
        else:
            referencesf(p, oids)
            f.writelines([oid, p64(len(p)), p])
    f.write(export_end_marker)
    return f

ExportImport.exportFile = exportFile

def _importDuringCommit(self, transaction, f, return_oid_list,
                        excluded_oids=()):
    """Import data during two-phase commit.

    Invoked by the transaction manager mid commit.
    Appends one item, the OID of the first object created,
    to return_oid_list.
    excluded_oids is a list of OIDs to totally ignore in the process.
    """
    oids = {}
    ooids = {} # GR reverse mapping is of our doing

    # IMPORTANT: This code should be consistent with the code in
    # serialize.py. It is currently out of date and doesn't handle
    # weak references.

    def persistent_load(ooid):
        """Remap a persistent id to a new ID and create a ghost for it."""

        klass = None
        if isinstance(ooid, tuple):
            ooid, klass = ooid

        if ooid in oids:
            oid = oids[ooid]
        else:
            if klass is None:
                oid = self._storage.new_oid()
            else:
                oid = self._storage.new_oid(), klass
            oids[ooid] = oid
            ooids[oid] = ooid

        return Ghost(oid)

    version = self._version

    while 1:
        h = f.read(16)
        if h == export_end_marker:
            break
        if len(h) != 16:
            raise ExportError("Truncated export file")
        l = u64(h[8:16])
        p = f.read(l)
        if len(p) != l:
            raise ExportError("Truncated export file")

        ooid = h[:8]
        if ooid in excluded_oids:
            continue
        if oids:
            oid = oids[ooid]
            if isinstance(oid, tuple):
                oid = oid[0]
        else:
            oids[ooid] = oid = self._storage.new_oid()
            return_oid_list.append(oid)

        pfile = StringIO(p)
        unpickler = Unpickler(pfile)
        unpickler.persistent_load = persistent_load

        newp = StringIO()
        pickler = Pickler(newp, 1)
        pickler.persistent_id = persistent_id

        kl = unpickler.load()
        attrs = unpickler.load()
        objects = attrs.get('_objects') # GR about ObjectManager only
        objects_changed = False
        for k, v in attrs.items():
            if v.__class__ != Ghost:
                continue
            ooid = ooids[v.oid]
            if ooid in excluded_oids:
                del attrs[k]
                if objects is not None:
                    objects = tuple(o for o in objects if o['id'] != k)
                    objects_changed = True

        if objects_changed:
            attrs['_objects'] = objects

        pickler.dump(kl)
        pickler.dump(attrs)
        p = newp.getvalue()

        self._storage.store(oid, None, p, version, transaction)

ExportImport._importDuringCommit = _importDuringCommit

def export(base, rpath, f, excluded=()):
    """Make a zexp export of an object to file f.

    f is the FS file path.
    base is a starting point object in the app.
    rpath is the relative path of the object to export, from base
    excluded is a list of relative paths of objects to avoid, from base

    return a list of oids to pass to the importer on the other side."""

    ob = base.unrestrictedTraverse(rpath)
    excluded_oids = [base.unrestrictedTraverse(e)._p_oid for e in excluded]
    f = ob._p_jar.exportFile(ob._p_oid, f, excluded_oids=excluded_oids)
    f.close()
    return excluded_oids

