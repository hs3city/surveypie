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
        the second Thiel measure or mean logarithmic deviation, and it assigns
        larger weights to the bottom part of the distribution. The parameter
        equal to 1 is the first Thiel measure - it assigns approximately equal
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
        Thiel Second Measure, and when set to 1 it calculates Thiel First
        Measure.

    Returns
    -------
    : EntropyIndex
    """
    if a == 0:
        return thiel_second_measure(data)
    elif a == 1:
        return thiel_first_measure(data)
    else:
        idx_1 = 1 / (a * (a - 1))
        idx_2 = len(data)
        p = idx_1 * idx_2
        mean_data = np.mean(data)
        index = p * np.sum(
            (data / mean_data) ** a - 1
        )
        eidx = EntropyIndex(index=index, a=a)
        return eidx


def thiel_first_measure(data: ArrayLike) -> EntropyIndex:
    """
    Function calculates Thiel First Measure - special case of Entropy Index,
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
    index = p1 * np.sum(
        (data / mu) * np.log2(data / mu)
    )
    eidx = EntropyIndex(index=index, a=1)
    return eidx


def thiel_second_measure(data: ArrayLike) -> EntropyIndex:
    """
    Function calculates Thiel Second Measure, or mean logarithmic deviation.
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
    index = p1 * np.sum(
        np.log2(mu / data)
    )
    return EntropyIndex(index=index, a=0)
