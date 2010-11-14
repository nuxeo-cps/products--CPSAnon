from Globals import InitializeClass
from AccessControl import ClassSecurityInfo
from Products.CMFCore.permissions import View
from Products.CPSCore.utils import bhasattr
from Products.CPSDocument.CPSDocument import CPSDocument

if not hasattr(CPSDocument, 'getDataModel'):
    security = ClassSecurityInfo()

    security.declareProtected(View, 'getDataModel')
    def getDataModel(self, proxy=None, REQUEST=None, **kw):
        """API convenience introduced in CPS 3.4 series.

        Taken from current CPS 3.5
        """

        if REQUEST:
            raise Unauthorized("Not accessible TTW.")

        ti = self.getTypeInfo()
        if ti is None:
            raise ValueError("No TI for portal_type %r" % self.portal_type)

        # It has to be an FTI in order to have the getDataModel method
        if bhasattr(ti, 'getDataModel'):
            return self.getTypeInfo().getDataModel(self, proxy=proxy)

        raise ValueError("%s is not a FTI : getDataModel is not available"
                         %(repr(ti)))

    CPSDocument.security = security
    CPSDocument.getDataModel = getDataModel
    InitializeClass(getDataModel)
