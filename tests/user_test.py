import unittest

from whoosh.query import Term
from user import User


class TestClassUser(unittest.TestCase):
    """Test User class"""

    def test_user_results(self):
        user = User()
        field = "alias"
        value = "Miss Dana"
        expected_length = 1
        id = 71
        results = user.search(Term(field, value))
        assert expected_length == len(results)
        assert id == results[0]["id"]


if __name__ == '__main__':
    unittest.main()
