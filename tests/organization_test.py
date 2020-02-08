import unittest

from whoosh.query import Term
from organization import Organization


class TestClassUser(unittest.TestCase):
    """Test User class"""

    def test_organization_results(self):
        org = Organization()
        field = "shared_tickets"
        value = "false"
        expected_length = 15
        results = org.search(Term(field, value))
        assert expected_length == len(results)


if __name__ == '__main__':
    unittest.main()
