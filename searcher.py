class Searcher:
    def __init__(self, indexer):
        self.indexer = indexer
        self.searcher = indexer.searcher()

    def search(self, term):
        return self.searcher.search(term, limit=None)
