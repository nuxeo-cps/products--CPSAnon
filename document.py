import csv
import logging

import transaction
from Products.CPSCore.ProxyBase import walk_cps_proxies
from Products.CPSAnon.random_content_generation import randomWords

logger = logging.getLogger(__name__)

class DocumentAnonymizer(object):
    """Provide methods to anonymize a hierarchy of documents.

    Proxies and their repository content are taken into account
    """

    txn_chunk_size = 100

    def __init__(self, portal):
        self.portal = portal
        self.fields_by_type = {}
        self.portal_type_column = None
        self.field_id_column = None
        self.trigger_column = None

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

    def run(self, rpath):
        """Anonymize the whole hierarchy under rpath and commit."""
        logger.info("Starting documents anonymization, rpath=%s", rpath)

        document_root = self.portal.restrictedTraverse(rpath)
        for c, proxy in enumerate(walk_cps_proxies(document_root)):
            self.docAnonymize(proxy)
            if c % self.txn_chunk_size == 0:
                transaction.commit()
        transaction.commit()


