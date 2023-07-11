import typing
from dataclasses import dataclass

import numpy


@dataclass
class AllisonFosterIndex:
    """
    Class representation of measures for Allison-Foster index
    index:  Allison-Foster index
    u_h: mean of the values above (H) group median value
    u_l: mean of the values below (L) group median value
    """

    index: float
    u_h: float
    u_l: float


def compute_measures(data: typing.Iterable) -> AllisonFosterIndex:
    """
    Function for computation Allison-Foster index and mean of the values
    above (H) group median value,
    mean of the values below (L) group median value
    Algorithm: Allison-Foster index = mean_h - mean_l
    :param data: List of values to compute Allison-Foster index from
    :return: Allison-Foster index, mean_h, mean_l
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

    return AllisonFosterIndex(allison_foster_index, mean_h, mean_l)
