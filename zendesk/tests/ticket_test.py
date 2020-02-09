import unittest

from whoosh.query import Term
from zendesk.ticket import Ticket


class TestClassTicket(unittest.TestCase):
    """Test Ticket class"""

    def test_ticket_results(self):
        user = Ticket()
        field = "assignee_id"
        value = 15
        expected_length = 5
        results = user.search(Term(field, value))
        assert expected_length == len(results)


if __name__ == '__main__':
    unittest.main()
