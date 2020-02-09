import os
import json

from zendesk.indexer import TicketIndexer
from zendesk.searcher import Searcher


class Ticket:
    """
    A class for tickets
    """
    def __init__(self):
        self.__schema = self.__get_schema()
        self.fields = self.__get_fields()
        self.__indexer = TicketIndexer()
        self.__searcher = Searcher(self.__indexer)

    @staticmethod
    def __get_schema():
        root_dir = os.path.dirname(os.path.abspath(__file__))
        tickets_schema_json = root_dir + "/data/schema/ticket.json.schema"
        with open(tickets_schema_json) as f:
            return json.load(f)

    def __get_fields(self):
        return self.__schema["properties"].keys()

    def search(self, query):
        """
        :return: results that match the query exactly
        """
        print("Searching tickets for", query)
        return self.__searcher.search(query)

    def print_fields(self):
        """
        :return: prints list of searchable fields
        """
        print(66 * "-")
        print("Ticket fields:")
        print("\n".join(self.fields), "\n")
        print(66 * "-")
