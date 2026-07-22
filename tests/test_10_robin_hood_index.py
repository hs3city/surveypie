import numpy as np
import pytest

from surveypie.robin_hood_index import RobinHoodIndex, robin_hood_index


def test_0_case():
    arr = np.zeros(3)
    g = robin_hood_index(arr)
    assert np.isnan(g.index)


def test_ones_case():
    arr = np.ones(30)
    g = robin_hood_index(arr)
    assert g.index == 0


def test_all_negative_case():
    arr = np.array([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])
    with pytest.raises(ValueError):
        _ = robin_hood_index(arr)


def test_one_negative_case():
    arr = np.array([1, 0, 1, -5])
    with pytest.raises(ValueError):
        _ = robin_hood_index(arr)


def test_real_numbers():
    arr = np.random.rand(100)
    g = robin_hood_index(arr)
    assert g.index >= 0


def test_gini_index_class():
    arr = np.random.rand(100)
    g = robin_hood_index(arr)
    assert isinstance(g, RobinHoodIndex)
    assert g.name == 'Robin Hood Index'
