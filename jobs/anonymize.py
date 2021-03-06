# (C) Copyright 2010 CPS-CMS Community <http://cps-cms.org/>
# Authors:
# M.-A. Darche <ma.darche@cynode.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
"""

import logging
import sys
import transaction

from Products.CMFCore.utils import getToolByName
from Products.CPSAnon import cpsjob # indirection for transparent backport

from Products.CPSAnon.document import DocumentAnonymizer

#from Products.CPSDirectory
#from cps.ldaputils import ldifanonymize

#from Products.CPSAnon import anon_map
v = {('userPassword', ('CHANGEME',)): '11',
     ('mail', ('Germaine.Gamout@gouv.fr',)): 'a15@example.net',
     ('uid', ('germaine.gamout',)): '5',
     ('description', ('Direction',)): '12',
     ('displayName', ('GAMOUT Germaine',)): '7',
     ('mail', ('ma.darche@example.com',)): 'a3@example.net',
     ('cn', ('GAMOUT Germaine',)): '8',
     ('sn', ('Darche',)): '2',
     ('givenName', ('Germaine',)): '16',
     ('title', ('Madame',)): '10',
     ('sn', ('GAMOUT',)): '14',
     ('uid', ('madarche',)): '0',
     ('businessCategory', ('BJ12',)): '9',
     ('telephoneNumber', ('01.09.09.09.09',)): '6',
     ('givenName', ('MAD',)): '4',
     ('cn', ('Darche',)): '1',
     ('employeeNumber', ('1',)): '13',
     }

ATTRS_TO_ANONYMIZE = (
    'uid', 'userid',
    'cn', 'commonname',
    'sn', 'surname',
    'givenname',
    'displayname',
    'l', 'localityname',
    'mail',
    'uid',
    'title',
    'employeenumber',
    'telephonenumber',
    'facsimiletelephonenumber',
    'description',
    'businesscategory',
    'roomnumber',
    'postaladdress',
    'userpassword',
)


logger = logging.getLogger(__name__)

def run(portal, options):
    if options.all:
        options.directories = options.documents = True

    if options.directories:
        anonymizeDirectories(portal, options)

    if options.documents:
        an = DocumentAnonymizer(portal)
        an.loadCsv(options.schema_fields_csv)
        if options.single_doc_rpath:
            an.docAnonymize(portal.restrictedTraverse(options.single_doc_rpath))
        else:
            an.run(options.document_root_rpath)

    transaction.commit()


def anonymizeDirectories(portal, options):
    logger.info("Starting directories anonymization")

    mtool = getToolByName(portal, 'portal_membership')
    dtool = getToolByName(portal, 'portal_directories')
    aclu = getToolByName(portal, 'acl_users')
    members_dir = aclu._getUsersDirectory()

    # The method returns a list of tuples containing the member id
    # and a dictionary of available fields:
    # [('member1', {'email': 'foo', 'age': 75}), ('member2', {'age': 5})]
    entries = members_dir.searchEntries(id='*', return_fields=['*'])
    for entry in entries:
        logger.info("entry = %s", entry)

        for attr_name, attr_value in entry[1].items():
            #if attr_name not in ldifanonymize.ATTRS_TO_ANONYMIZE:
            if attr_name not in ATTRS_TO_ANONYMIZE:
                continue

            # TODO: The directory fields and the map fields must be mapped
            # through some schema mapping.

            anonymization_map_key = (attr_name, tuple([attr_value]))
            logger.info("anonymization_map_key = %s", anonymization_map_key)

            if v.get(anonymization_map_key) is None:
                continue

            entry_values = entry[1]
            entry_values[attr_name] = v[anonymization_map_key]

            logger.info("entry_values = %s", entry_values)

            # Saving the modified entry in the directory
            members_dir.editEntry(entry_values)

            # TODO: If the id of the entry is to be modified: delete the entry
            # and create a new one with a new id.

def main():
    """cpsjob bootstrap."""
    optparser = cpsjob.optparser
    optparser.add_option('-d', '--directories', dest='directories',
                         action='store_true',
                         help="Anonymize directories")

    optparser.add_option('-w', '--documents', dest='documents',
                         action='store_true',
                         help="Anonymize documents")

    optparser.add_option('-c', '--csvfile',
                         action='store',
                         dest='schema_fields_csv',
                         type='string',
                         metavar='FILE',
                         help="Use FILE as the filename for "
                         "the schema fields CSV file to use "
                         "to know which field to anonymize")

    optparser.add_option('-p', '--limit-to-rpath', dest='document_root_rpath',
                         action='store',
                         type='string',
                         default='',
                         metavar='RPATH',
                         help="Limit the document anonymization to documents "
                         "under the given RPATH")

    optparser.add_option('-a', '--all', dest='all', action='store_true',
                         help="Run everything")

    optparser.add_option('--single-document', dest='single_doc_rpath',
                         metavar='RPATH',
                         help="Anonymize one single document, at the given "
                         "RPATH. Incompatible with --limit-to-rpath")

    portal, options, args = cpsjob.bootstrap(app)

    if args:
        optparser.error("Args: %s; this job accepts one argument only"
                        " (portal id) "
                        "Try --help" % ' '.join(args))

    if options.schema_fields_csv is None:
        optparser.error("--csvfile option is mandatory. Try --help.")

    if options.single_doc_rpath and options.document_root_rpath:
        optparser.error("Incompatible options. Try --help.")

    run(portal, options)

# invocation through zopectl run
if __name__ == '__main__':
    main()

