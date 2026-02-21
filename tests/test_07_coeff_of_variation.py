import numpy as np
import pytest

from surveypie.cov import coeff_of_variation


def test_0_case():
    arr = np.zeros(10)
    with pytest.raises(ZeroDivisionError):
        _ = coeff_of_variation(arr)


def test_1_case():
    arr = np.ones(10)
    cov = coeff_of_variation(arr)
    # 0/1
    assert cov == 0


def test_5_case():
    arr = np.ones(10) * 5
    cov = coeff_of_variation(arr)
    # 0/5
    assert cov == 0


def test_random_int_case():
    arr = np.random.randint(low=1, high=10, size=100)
    cov = coeff_of_variation(arr)
    assert cov > 0
    assert isinstance(cov, float)


def test_weighted_case_zeros():
    arr = np.random.randint(low=1, high=10, size=100)
    weights = np.zeros(len(arr))
    with pytest.raises(ZeroDivisionError):
        _ = coeff_of_variation(arr, weights)


def test_weighted_case_ones():
    arr = np.random.randint(low=1, high=10, size=100)
    weights = np.ones(len(arr))

    cov = coeff_of_variation(arr)
    w_cov = coeff_of_variation(arr, weights=weights)
    assert cov == w_cov


def test_weighted_case_negative_weights():
    arr = np.random.randint(low=1, high=10, size=100)
    weights = np.random.randint(low=-10, high=-1, size=len(arr))
    with pytest.raises(ValueError):
        _ = coeff_of_variation(arr, weights=weights)
