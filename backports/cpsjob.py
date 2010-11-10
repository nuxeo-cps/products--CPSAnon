"""This is meant to be used in conjunction with zopectl run

BACKPORT as a simple copy of current version (3.5.2-devel, CPSUtil 1.8.0)
for versions before 3.5

Can be invocated directly instead of Zope2/Startup/zopectl.py,
or used as a toolkit by zopectl run scripts.
In particular, there is an OptionParser instance and a bootstrap function, to
be used along these lines:

>>> from Products.CPSUtil import cpsjob
>>> cpsjob.optparser.add_option('-e', '--example', dest='exmp', default='val')
>>> portal, options, arguments = cpsjob.bootstrap(app)

The bootstrap function uses the first positional arg of the script as the name
of the CPS portal. Scripts for which this behaviour would be found useless
or obstrusive can of course import directly some of the lower level helper
functions.

An external method can be applied simply like this:

>>> from Products.CPSUtil import cpsjob
>>> portal, options, arguments = cpsjob.bootstrap(app)
>>> portal.my_external_method()
>>> import transaction; transaction.commit()

Don't forget the commit in this case, since it's usually automatic in the
context external methods are normally launched in.
"""

import sys
import os
import logging
logger = logging.getLogger(__name__)

import optparse
optparser = optparse.OptionParser(
    usage="usage: %prog [options] <portal id> [job args]")
optparser.add_option('-u', '--username', dest='user_id', default='cpsjob',
                     help="the identifier of the transient unrestricted "
                     "user to run as (will appear, e.g, in "
                     "status history of modified documents). "
                     "Defaults to '%default'."
                     )
optparser.add_option('--loglevel', dest='log_level', default='INFO',
                     help="Log level (standard logging module levels)"
                     "Defaults to '%default'."
                     )

# Taken from ZopeTestCase.
# Not imported because import as side-effect of switching to testing ZODB
def makerequest(app, stdout=sys.stdout, host=None, port=None):
    '''Wraps the app into a fresh REQUEST.'''
    from ZPublisher.BaseRequest import RequestContainer
    from ZPublisher.Request import Request
    from ZPublisher.Response import Response
    response = Response(stdout=stdout)
    environ = {}
    environ['SERVER_NAME'] = host or 'nohost'
    environ['SERVER_PORT'] = '%d' % (port or 80)
    environ['REQUEST_METHOD'] = 'GET'
    request = Request(sys.stdin, environ, response)
    request._steps = ['noobject'] # Fake a published object
    request['ACTUAL_URL'] = request.get('URL') # Zope 2.7.4

    # set Zope3-style default skin so that the request is usable for
    # Zope3-style view look-ups
    try:
        from zope.app.publication.browser import setDefaultSkin
    except ImportError:
        logger.warn("Very old version : Zope 3 views not tied to this "
                    "Request objects")
    else:
        setDefaultSkin(request)

    return app.__of__(RequestContainer(REQUEST=request))


def get_portal(app, portal_id):
    app = makerequest(app)
    try:
        from Products.CPSCore.portal import CPSSite
    except ImportError:
        from Products.CPSDefault.Portal import CPSDefaultSite as CPSSite

    try:
        return getattr(app, portal_id)
    except AttributeError:
        found = False
    else:
        found = True

    if not found or not isinstance(portal, CPSSite):
        raise RuntimeError("Not the id of a CPS portal : '%s'", portal_id)

def login(portal, user_id, roles=('Manager', 'Member')):
    """Lookup and log user in.
    This is done first from root user folder, then from CPS' to avoid
    lenghty timeouts in case of broken LDAP setups and the like."""

    from AccessControl.SecurityManagement import newSecurityManager
    app = portal.unrestrictedTraverse('/')
    aclu = app.acl_users
    user = aclu.getUser(user_id)
    if user is None:
        aclu = portal.acl_users
        user = aclu.getUser(user_id)

    if user is None:
        raise ValueError('Could not find user %r' % user_id)
    user = user.__of__(aclu)
    if not user.has_role('Manager'):
        raise ValueError('User %r not a Manager' % user_id)
    newSecurityManager(None, user)

def configure_logging(level):
    """Needs INSTANCE_HOME to be set"""

    handler = logging.FileHandler(
        os.path.join(INSTANCE_HOME, 'log', 'cpsjob.log'))

    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)-8s %(message)s',
                                  )#datefmt='%a, %d %b %Y %H:%M:%S',)
    handler.setFormatter(formatter)

    for path in ('', 'Products'):
        logger = logging.getLogger(path)
        logger.setLevel(getattr(logging, level.upper()))
        logger.addHandler(handler)

def parse_args():
    options, arguments = optparser.parse_args()
    if len(arguments) < 1:
	optparser.error("Incorrect number of arguments. Use -h for long help")
    return options, arguments

def bootstrap(app):
    """To be launched via zopectl run.

    Return portal, options, positional arguments
    """
    options, arguments = parse_args()
    configure_logging(options.log_level)

    portal = get_portal(app, arguments[0])
    login(portal, options.user_id)
    return portal, options, arguments[1:]

if __name__ == '__main__':
    parse_args() # what else could we do without the app object ?
