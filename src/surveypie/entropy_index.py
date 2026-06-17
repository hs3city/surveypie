from numpy.typing import ArrayLike
import numpy as np

from surveypie.structure.index_model import BaseIndex


class EntropyIndex(BaseIndex):
    """
    Entropy Index metadata

    Attributes
    ----------
    index : float
        Entropy index.

    name : str = 'Generalized entropy index'

    a : float
        Parameter controlling sensitivity to income levels: large `a` is
        especially sensitive to existence of large incomes, and small
        `a` is sensitive to small incomes. The parameter equal to 0 is
        the second Theil measure or mean logarithmic deviation, and it assigns
        larger weights to the bottom part of the distribution. The parameter
        equal to 1 is the first Theil measure - it assigns approximately equal
        weights to all parts of the distribution. In cases when `a` is larger
        than 1 it becomes more sensitive to existence of large outliers in
        the distribution.

    """

    name: str = "Generalized entropy index"
    a: float = np.nan


def entropy_index(data: ArrayLike, a: float) -> EntropyIndex:
    """
    Entropy Index calculation.

    Parameters
    ----------
    data : ArrayLike
        Vector with data.

    a : float
        Parameter controlling the entropy index, lower values equal or lower
        than 0 are more sensitive to the existence of observations with a small
        intensity (e.g. very low incomes). Large `a` value, greater than 1
        makes it more sensitive to the existence of large outliers
        (e.g. extremely high incomes). When set to 0 then it calculates
        Theil Second Measure, and when set to 1 it calculates Theil First
        Measure.

    Returns
    -------
    : EntropyIndex
    """
    if a == 0:
        return theil_second_measure(data)
    elif a == 1:
        return theil_first_measure(data)
    else:
        idx_1 = 1 / (a * (a - 1))
        idx_2 = 1 / len(data)
        p = idx_1 * idx_2
        mu = np.mean(data)
        if mu == 0:
            raise ZeroDivisionError(
                "Mean of data is equal to 0, "
                "cannot proceed due to "
                "the numerical instability - "
                "division by zero."
            )

        index = p * np.sum((data / mu) ** a - 1)
        eidx = EntropyIndex(index=index, a=a)
        return eidx


def theil_first_measure(data: ArrayLike) -> EntropyIndex:
    """
    Function calculates Theil First Measure - special case of Entropy Index,
    where almost equal weights are assigned to all parts of the distribution.

    Parameters
    ----------
    data : ArrayLike
        Vector with data.

    Returns
    -------
    : EntropyIndex
    """
    p1 = 1 / (len(data))
    mu = np.mean(data)
    if mu == 0:
        raise ZeroDivisionError(
            "Mean of data is equal to 0, " "cannot proceed due to " "the numerical instability - " "division by zero."
        )

    index = p1 * np.sum((data / mu) * np.log2(data / mu))
    eidx = EntropyIndex(index=index, a=1)
    return eidx


def theil_second_measure(data: ArrayLike) -> EntropyIndex:
    """
    Function calculates Theil Second Measure, or mean logarithmic deviation.
    This is a special case of Entropy Index, where larger weights are assigned
    to the bottom part of a distribution (e.g. low incomes).

    Parameters
    ----------
    data : ArrayLike
        Vector with data.

    Returns
    -------
    : EntropyIndex
    """
    p1 = 1 / (len(data))
    mu = np.mean(data)
    if mu == 0:
        raise ValueError("Trying to get log2(0), " "cannot proceed due to " "the numerical instability.")

    index = p1 * np.sum(np.log2(mu / data))
    return EntropyIndex(index=index, a=0)
