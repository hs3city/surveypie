import statistics
import typing
from dataclasses import dataclass


@dataclass
class AllisonFosterMeasures:
    """
    Class representation of measures for Allison-Foster index
    index:  Allison-Foster index
    mean_h: mean of the values above (H) group median value
    mean_l: mean of the values below (L) group median value
    """

    index: float
    mean_h: float
    mean_l: float


def compute_measures(data: typing.List) -> AllisonFosterMeasures:
    """
    Function for computation Allison-Foster index and mean of the values above (H) group median value,
    mean of the values below (L) group median value
    Algorithm: Allison-Foster index = mean_h - mean_l
    :param data: List of values to compute Allison-Foster index from
    :return: Allison-Foster index, mean_h, mean_l
    """
    median_value = statistics.median(data)
    values_above_median = [value for value in data if value > median_value]
    values_below_median = [
        value
        for value in data
        if value not in values_above_median and value != median_value
    ]

    mean_h = statistics.mean(values_above_median)
    mean_l = statistics.mean(values_below_median)
    allison_foster_index = mean_h - mean_l

    return AllisonFosterMeasures(allison_foster_index, mean_h, mean_l)
