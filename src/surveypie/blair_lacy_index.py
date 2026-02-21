"""
Blair and Lacy Index implementation.

Author: Szymon Moliński (@SimonMolinsky)

Version: 1.0

Last Revision: 2026-01-31

Contributors:
  - Szymon Moliński (@SimonMolinsky)

Tutorials:
  - ``blair-and-lacy-index``
"""

from numpy.typing import ArrayLike

from surveypie.core import info
from surveypie.structure.index_model import BaseIndex

import numpy as np


class BlairLacyIndex(BaseIndex):
    """
    Blair and Lacy Index metadata

    Attributes
    ----------
    index : float
        Blair and Lacy index. Describes dataset dispersion. Index closer to
        zero means that the dispersion is minimal, and index closer to one
        means that the dispersion is maximal.

    name : str = 'Blair and Lacy Index'

    index_sqrt : float
        Blair and Lacy Index - square root of the concentration measure.

    l2_index : floar
        Blair and Lacy dispersion measure before subtraction (`index`
        parameter is equal to one minus `l2_index`).

    min_dispersion : float
        The maximum possible value of `index_sq`, all records fall into a
        single ordinal category, minimal dispersion
    """

    name: str = "Blair and Lacy Index"
    index_sqrt: float = np.nan
    l2_index: float = np.nan
    min_dispersion: float = np.nan


def bl_index(categories: ArrayLike, responses: ArrayLike) -> BlairLacyIndex:
    r"""
    Blair and Lacy inequality measure.

    Parameters
    ----------
    categories : array
        Ordered list of possible categories.

    responses : array
        Dataset with ordinal-scale values used for index computation.

    Returns
    -------
    index : BlairLacyIndex
        Index and index squared.

    Notes
    -----
    Index is calculated as:

    $$I = 1 - \frac{\sum_{i=1}^{n-1} (P_{i}-0.5)^2)}{\frac{n-1}{4}}$$

    and

    $$I_{sqrt} = 1 - (\frac{\sum_{i=1}^{n-1} (P_{i}-0.5)^2)}{\frac{n-1}{4}})^{0.5}$$

    where:
    - $I$ - normalized dispersion measure, when it is close to 0 then
      the dispersion is minimum, and when value is closer to 1 then
      the dispersion is maximum. More sensitive to changes in the distribution
      when the dispersion is low
    - $I_{sqrt}$ - square root of normalized dispersion measure, when it is close
      to 0 then the dispersion is minimum, and when value is closer to 1 then
      the dispersion is maximum. More sensitive to changes in the distribution
      when the dispersion is high
    - $P_{i}$ - the cumulative distribution of *i-th* category
    - $\frac{n-1}{4}$ - is the maximum possible value of $I_{sq}$, all
      records fall into a single ordinal category, minimal dispersion

    References
    ----------
    Blair J, Lacy M G. (2000): Statistics of ordinal variation,
    Sociological Methods and Research 28(251);251-280

    """

    categories = np.array(categories)
    categories = np.sort(categories)

    n_categories = len(categories)

    ds = info(responses=responses, indicators=categories)
    ds = ds["cumulative"]

    denom = (n_categories - 1) / 4

    num = (ds.values[:-1] - 0.5) ** 2
    num_sum = np.sum(num)
    l2 = num_sum / denom

    index = 1 - l2
    index_sqrt = 1 - np.sqrt(l2)

    return BlairLacyIndex(index=index, index_sqrt=index_sqrt, l2_index=l2, min_dispersion=denom, n_classes=n_categories)
