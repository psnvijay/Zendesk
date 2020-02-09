import os
import json

from indexer import OrganizationIndexer
from searcher import Searcher


class Organization:
    """
    A class for organizations
    """
    def __init__(self):
        self.__schema = self.__get_schema()
        self.fields = self.__get_fields()
        self.__indexer = OrganizationIndexer()
        self.__searcher = Searcher(self.__indexer)

    @staticmethod
    def __get_schema():
        users_schema_json = os.getcwd() + "/data/schema/organization.json.schema"
        with open(users_schema_json) as f:
            return json.load(f)

    def __get_fields(self):
        return self.__schema["properties"].keys()

    def search(self, query):
        """
        :return: results that match the query exactly
        """
        print("Searching organizations for", query)
        return self.__searcher.search(query)

    def print_fields(self):
        """
        :return: prints list of searchable fields
        """
        print(66 * "-")
        print("Organization fields:")
        print("\n".join(self.fields), "\n")
        print(66 * "-")