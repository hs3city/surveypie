from src.apouey_index import get_apouey_index
import unittest

DS = []
DS.extend(10 * [1])
DS.extend(10 * [2])
DS.extend(10 * [3])
DS.extend(5 * [4])
DS.extend(15 * [5])

INDICATORS = [1, 2, 3, 4, 5]


def test_apouey_positive():
    assert round(get_apouey_index(INDICATORS, DS), 3) == 0.673


class ApoueyTestCase(unittest.TestCase):
    def test_apouey_negative(self):
        with self.assertRaises(AttributeError):
            get_apouey_index(categories=[1], responses=DS)
            get_apouey_index(
                categories=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], responses=DS
            )
