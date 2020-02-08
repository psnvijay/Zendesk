import os

from abc import ABC, abstractmethod
from whoosh.fields import Schema, ID, BOOLEAN, NUMERIC
from whoosh import index


class Indexer(ABC):
    """
    Abstract class for creating an index
    """
    def __init__(self):
        """
        Constructor for the Indexer class
        """
        self.base_dir = os.getcwd() + "/data/index/"  # base directory location for all indexes

    @abstractmethod
    def index(self, data):
        pass


class UserIndexer(Indexer):
    """
    Class for creating user index
    """
    def __init__(self):
        """
        Constructor for the UserIndexer class
        """
        super().__init__()
        self.index_dir = self.base_dir + "user/"
        self.index_schema = self.__get_index_schema()
        if not os.path.exists(self.index_dir):
            os.mkdir(self.index_dir)
            self.indexer = index.create_in(self.index_dir, self.index_schema)  # creates the index
        else:
            self.indexer = index.open_dir(self.index_dir)  # opens the index if it already exists

    def __get_index_schema(self):
        """
        :return: user index schema
        """
        return Schema(id=NUMERIC(stored=True),
                      url=ID(stored=True),
                      external_id=ID(stored=True),
                      name=ID(stored=True),
                      alias=ID(stored=True),
                      created_at=ID(stored=True),
                      active=BOOLEAN(stored=True),
                      verified=BOOLEAN(stored=True),
                      shared=BOOLEAN(stored=True),
                      locale=ID(stored=True),
                      timezone=ID(stored=True),
                      last_login_at=ID(stored=True),
                      email=ID(stored=True),
                      phone=ID(stored=True),
                      signature=ID(stored=True),
                      organization_id=NUMERIC(stored=True),
                      tags=ID(stored=True),
                      suspended=BOOLEAN(stored=True),
                      role=ID(stored=True))

    def index(self, data):
        """
        indexes user data
        :param data: A list of dicts to index
        """
        writer = self.indexer.writer()
        for document in data:
            writer.add_document(**document)
        writer.commit()

    def searcher(self):
        return self.indexer.searcher()


class TicketIndexer(Indexer):
    """
    Class for creating ticket index
    """
    def __init__(self):
        """
        Constructor for the TicketIndexer class
        """
        super().__init__()
        self.index_dir = self.base_dir + "ticket/"
        self.index_schema = self.__get_index_schema()
        if not os.path.exists(self.index_dir):
            os.mkdir(self.index_dir)
            self.indexer = index.create_in(self.index_dir, self.index_schema)
        else:
            self.indexer = index.open_dir(self.index_dir)

    def __get_index_schema(self):
        """
        :return: ticket index schema
        """
        return Schema(status=ID(stored=True),
                      assignee_id=NUMERIC(stored=True),
                      via=ID(stored=True),
                      description=ID(stored=True),
                      tags=ID(stored=True),
                      url=ID(stored=True),
                      external_id=ID(stored=True),
                      created_at=ID(stored=True),
                      submitter_id=NUMERIC(stored=True),
                      priority=ID(stored=True),
                      due_at=ID(stored=True),
                      organization_id=NUMERIC(stored=True),
                      has_incidents=BOOLEAN(stored=True),
                      id=ID(stored=True),
                      type=ID(stored=True),
                      subject=ID(stored=True))

    def index(self, data):
        """
        indexes ticket data
        :param data: A list of dicts to index
        """
        writer = self.indexer.writer()
        for document in data:
            writer.add_document(**document)
        writer.commit()

    def searcher(self):
        return self.indexer.searcher()


class OrganizationIndexer(Indexer):
    """
    Class for creating organization index
    """
    def __init__(self):
        super().__init__()
        self.index_dir = self.base_dir + "organization/"
        self.index_schema = self.__get_index_schema()
        if not os.path.exists(self.index_dir):
            os.mkdir(self.index_dir)
            self.indexer = index.create_in(self.index_dir, self.index_schema)
        else:
            self.indexer = index.open_dir(self.index_dir)

    def __get_index_schema(self):
        """
        :return: organization index schema
        """
        return Schema(
            id=NUMERIC(stored=True),
            url=ID(stored=True),
            external_id=ID(stored=True),
            name=ID(stored=True),
            domain_names=ID(stored=True),
            created_at=ID(stored=True),
            details=ID(stored=True),
            shared_tickets=BOOLEAN(stored=True),
            tags=ID(stored=True))

    def index(self, data):
        """
        indexes organization data
        :param data: A list of dicts to index
        """
        writer = self.indexer.writer()
        for document in data:
            writer.add_document(**document)
        writer.commit()

    def searcher(self):
        return self.indexer.searcher()
