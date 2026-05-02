import numpy as np
import pytest

from surveypie.entropy_index import entropy_index, EntropyIndex


def test_0_a1_case():
    a = 1
    arr = np.zeros(3)
    with pytest.raises(ZeroDivisionError):
        _ = entropy_index(arr, a=a)


def test_0_a0_case():
    a = 0
    arr = np.zeros(3)
    with pytest.raises(ValueError):
        _ = entropy_index(arr, a=a)


def test_0_an_cases():
    a_s = [-2, -1, 2, 4]
    arr = np.zeros(3)
    for a in a_s:
        with pytest.raises(ZeroDivisionError):
            _ = entropy_index(arr, a=a)


def test_1_a1_case():
    a = 1
    arr = np.ones(3)
    index = entropy_index(arr, a=a)
    assert index.index == 0
    assert isinstance(index, EntropyIndex)


def test_1_a0_case():
    a = 0
    arr = np.ones(3)
    index = entropy_index(arr, a=a)
    assert index.index == 0
    assert isinstance(index, EntropyIndex)


def test_1_an_cases():
    a_s = [-2, -1, 2, 4]
    arr = np.ones(3)
    for a in a_s:
        index = entropy_index(arr, a=a)
        assert index.index == 0
        assert isinstance(index, EntropyIndex)


def test_randint_greater_equal_0_an_cases():
    a_s = np.arange(-11, 11)
    arr = np.random.randint(low=0, high=1000, size=50)
    for a in a_s:
        index = entropy_index(arr, a=a)
        assert index.index != 0
        assert isinstance(index, EntropyIndex)


def test_randint_lower_than_0_an_cases():
    a_s = np.arange(-11, 11)
    arr = np.random.randint(low=-10, high=0, size=50)
    for a in a_s:
        index = entropy_index(arr, a=a)
        assert index.index != 0
        assert isinstance(index, EntropyIndex)
