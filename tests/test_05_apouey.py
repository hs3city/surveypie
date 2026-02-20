from surveypie.apouey_index import ap_index
import unittest


DS = []
DS.extend(10 * [1])
DS.extend(10 * [2])
DS.extend(10 * [3])
DS.extend(5 * [4])
DS.extend(15 * [5])

INDICATORS = [1, 2, 3, 4, 5]


def test_apouey_positive():
    assert round(ap_index(INDICATORS, DS), 3) == 0.545


class ApoueyTestCase(unittest.TestCase):
    def test_apouey_negative(self):
        with self.assertRaises(ValueError):
            ap_index(categories=[1], responses=DS)
            ap_index(
                categories=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], responses=DS
            )
