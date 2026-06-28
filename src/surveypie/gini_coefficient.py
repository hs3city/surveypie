from numpy.typing import ArrayLike
import numpy as np

from surveypie.structure.index_model import BaseIndex


class GiniIndex(BaseIndex):
    """
    Gini Coefficient metadata

    Attributes
    ----------
    index : float
        Gini coefficient.

    name : str = 'Gini coefficient'

    """

    name: str = "Generalized entropy index"
    a: float = np.nan


def gini_coefficient(data: ArrayLike) -> GiniIndex:
    """
    Gini coeffcient calculation (the population Gini coeffcient)

    Parameters
    ----------
    data : ArrayLike
        Vector with data.

    Returns
    -------
    : GiniIndex
    """

    n = len(data)
    d = np.sort(data)
    r = np.arange(1, n)
    g = (2 * np.dot(d, r)) / (n * np.sum(d)) - ((n + 1) / n)
    return g


if __name__ == "__main__":
    ...
