"""
Allison-Foster Index implementation.

Author: Marta Leszczyńska (@Reckony)

Version: 1.1

Last Revision: 2024-02-04

Contributors:
  - Szymon Moliński (@SimonMolinsky)

Tutorials:
  - ``allison-foster-index``
"""
from numpy.typing import ArrayLike
from src.index_model import BaseIndex

import numpy


class AllisonFosterIndex(BaseIndex):
    """
    Allison-Foster Index metadata

    Attributes
    ----------
    index : float
        Allison-Foster index.

    name : str = 'Allison-Foster Index'

    u_h : float
        The mean of the values above (H) group median value.

    u_l : float
        The mean of the values below (L) group median value.
    """

    u_h: float
    u_l: float
    name: str = "Allison-Foster Index"


def af_index(data: ArrayLike) -> AllisonFosterIndex:
    """
    Function for computation Allison-Foster index.

    Parameters
    ----------
    data : array like
        Dataset with ordinal-scale values used for index computation.

    Returns
    -------
    BaseIndex : Allison Foster Index

    Notes
    -----
    Index is calculated as a difference between the mean of the values
    above group median value (H) and the mean of the values below (L) group
    median value.

    Algorithm: AF = MEAN(H) - MEAN(L)
    """
    median_value = numpy.median(data)
    values_above_median = [value for value in data if value > median_value]
    values_below_median = [
        value
        for value in data
        if value not in values_above_median and value != median_value
    ]

    mean_h = float(numpy.mean(values_above_median))
    mean_l = float(numpy.mean(values_below_median))
    allison_foster_index = mean_h - mean_l

    return AllisonFosterIndex(
        index=allison_foster_index, u_h=mean_h, u_l=mean_l
    )
