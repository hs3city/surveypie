from numpy.typing import ArrayLike
import numpy as np
from pydantic import field_validator

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


def entropy_index(data: ArrayLike, a: float):
    """
    Entropy Index calculation.

    Parameters
    ----------
    data : ArrayLike
        Vector with data.

    a : float
        Parameter controlling the entropy index.

    Returns
    -------

    """
    ...


def thiel_first_measure():
    ...

def thiel_second_measure():
    ...
