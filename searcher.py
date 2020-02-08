class Searcher:
    """
    A class to search on index
    """
    def __init__(self, indexer):
        """
        The constructor for Searcher class

        :param indexer: Index to search on
        """
        self.indexer = indexer
        self.searcher = indexer.searcher()

    def search(self, query):
        """
        :param query: search query
        :return: all search results
        """
        return self.searcher.search(query, limit=None)  # limit = None returns all search results
