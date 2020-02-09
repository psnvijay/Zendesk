import os
import json

from indexer import UserIndexer
from searcher import Searcher


class User:
    """
    A class for users
    """
    def __init__(self):
        self.__schema = self.__get_schema()
        self.fields = self.__get_fields()
        self.__indexer = UserIndexer()
        self.__searcher = Searcher(self.__indexer)

    @staticmethod
    def __get_schema():
        root_dir = os.path.dirname(os.path.abspath(__file__))
        users_schema_json = root_dir + "/data/schema/user.json.schema"
        with open(users_schema_json) as f:
            return json.load(f)

    def __get_fields(self):
        return self.__schema["properties"].keys()

    def search(self, query):
        """
        :return: results that match the query exactly
        """
        print("Searching users for", query)
        return self.__searcher.search(query)

    def print_fields(self):
        """
        :return: prints list of searchable fields
        """
        print(66 * "-")
        print("User fields:")
        print("\n".join(self.fields), "\n")
        print(66 * "-")


