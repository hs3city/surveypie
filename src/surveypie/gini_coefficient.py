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

    name: str = "Gini Index"


def gini_index(data: ArrayLike) -> GiniIndex:
    """
    Gini coeffcient calculation (the population Gini coeffcient).

    Parameters
    ----------
    data : ArrayLike
        Vector with data.

    Returns
    -------
    : GiniIndex

    References
    ----------
    1. Kendall, Maurice G., and Alan Stuart. 1958.
       The Advanced Theory of Statistics. Vol. 1, Distribution Theory.
    2. Gini, C. (1912). Variabilità e mutabilità [Variability and Mutability].
    """

    n = len(data)
    d = np.sort(data)

    if d[0] < 0:
        raise ValueError(
            "Negative values passed into input data array, remove those "
            "or set to zero before calculating Gini index, or change the "
            "inequality index altogether."
        )

    r = np.arange(1, n + 1)
    num = 2 * np.dot(d, r)
    denom = n * np.sum(d)
    if denom == 0:
        raise ZeroDivisionError(
            "Denominator in equation is equal to 0, " "cannot proceed due to " "the numerical instability."
        )
    g = num / denom - ((n + 1) / n)
    gi = GiniIndex(index=g)
    return gi
