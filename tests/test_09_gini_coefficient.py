import numpy as np
import pytest

from surveypie.gini_coefficient import gini_index, GiniIndex


def test_0_case():
    arr = np.zeros(3)
    with pytest.raises(ZeroDivisionError):
        _ = gini_index(arr)


def test_ones_case():
    arr = np.ones(30)
    g = gini_index(arr)
    assert g.index == 0


def test_all_negative_case():
    arr = np.array([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])
    with pytest.raises(ValueError):
        _ = gini_index(arr)


def test_one_negative_case():
    arr = np.array([1, 0, 1, -5])
    with pytest.raises(ValueError):
        _ = gini_index(arr)


def test_allow_negative_case():
    arr = np.array([1, 0, 1, -50])
    g = gini_index(arr, allow_negative=True)
    assert g.index < 0


def test_real_numbers():
    arr = np.random.rand(100)
    g = gini_index(arr)
    assert g.index >= 0


def test_gini_index_class():
    arr = np.random.rand(100)
    g = gini_index(arr)
    assert isinstance(g, GiniIndex)
    assert g.name == 'Gini Index'
