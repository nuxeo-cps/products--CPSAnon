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

import csv

import logging
import sys
import transaction

from Products.CMFCore.utils import getToolByName
from Products.CPSAnon import cpsjob # indirection for transparent backport
from Products.CPSCore.ProxyBase import walk_cps_proxies

from Products.CPSAnon.random_content_generation import randomWords

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
        DocumentAnonymizer(portal, options).run()

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

class DocumentAnonymizer(object):

    txn_chunk_size = 100

    def __init__(self, portal, options):
        self.portal = portal
        self.options = options
        self.fields_by_type = {}
        self.portal_type_column = None
        self.field_id_column = None
        self.trigger_column = None
        self.loadCsv(options.schema_fields_csv)

    def loadCsv(self, fpath):
        # First create an object mapping from the CSV file
        #
        # Structure type
        #v = { 'type1': ['field1', 'field2'],
        #      'type2': ['field1', 'field2', 'field3'],
        #     }

        reader = csv.reader(open(fpath, 'rb'))

        for line_number, row in enumerate(reader):
            # First row determines which columns represents what
            if line_number == 0:
                logger.info("row = %s", row)
                column_number = 0
                for column in row:
                    if column.lower() == 'type':
                        self.portal_type_column = column_number
                    elif column.lower() in ('fid', 'field id'):
                        self.field_id_column = column_number
                    elif column.lower() == 'ano':
                        self.trigger_column = column_number
                    column_number += 1

                if (self.portal_type_column is None or
                    self.field_id_column is None or
                    self.trigger_column is None):
                    raise ValueError("Bad column format in the CSV file")
                else:
                    logger.info("portal_type_column = %s, "
                                "field_id_column = %s, "
                                "trigger_column = %s",
                                self.portal_type_column,
                                self.field_id_column,
                                self.trigger_column)
                continue

            if row[self.trigger_column]:
                portal_type = row[self.portal_type_column]
                fields = self.fields_by_type.setdefault(portal_type, [])
                fields.append(row[self.field_id_column])

        logger.info("fields_by_types_to_anonymize = %s", self.fields_by_type)


    def docAnonymize(self, proxy):
        logger.info("considering proxy = %s", proxy)

        field_ids = self.fields_by_type.get(proxy.portal_type)
        if field_ids is None:
            return

        logger.info("Will anonymize proxy = %s", proxy)

        dm = proxy.getContent().getDataModel(proxy=proxy)
        for field_id in field_ids:
            dm[field_id] = ' '.join(randomWords())

        # _commitData writes in the repository whether the document
        # is frozen or not.
        dm._commitData()

        logger.info("Has anonymized proxy = %s", proxy)

    def run(self):
        logger.info("Starting documents anonymization")
        if self.options.document_root_rpath:
            document_root = self.portal.restrictedTraverse(
                self.options.document_root_rpath)
        else:
            document_root = self.portal

        for c, proxy in enumerate(walk_cps_proxies(document_root)):
            self.docAnonymize(proxy)
            if c % self.txn_chunk_size == 0:
                transaction.commit()


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
                         metavar='RPATH',
                         help="Limit the document anonymization to documents "
                         "under the given RPATH")

    optparser.add_option('-a', '--all', dest='all', action='store_true',
                         help="Run everything")

    portal, options, args = cpsjob.bootstrap(app)

    if args:
        optparser.error("Args: %s; this job accepts options only."
                        "Try --help" % args)

    run(portal, options)

# invocation through zopectl run
if __name__ == '__main__':
    main()

