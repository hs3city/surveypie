from src.apouey_index import get_apouey_index
import unittest

responses = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
    4, 4, 4, 4, 4,
    5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5
]


def test_apouey_positive():
    assert get_apouey_index(categories=5, responses=responses) == 0.55


class ApoueyTestCase(unittest.TestCase):
    def test_apouey_negative(self):
        with self.assertRaises(AttributeError):
            get_apouey_index(categories=1, responses=responses)
            get_apouey_index(categories=11, responses=responses)
