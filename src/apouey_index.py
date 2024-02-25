import numpy as np
from typing import Sequence
from src.core import info
from numpy.typing import ArrayLike

ALPHA_LOOKUP_TABLE = {
    3: round(np.log(2) / np.log(3), 2),
    4: round((np.log(4) - np.log(3) / np.log(2)), 2),
    5: 0.73,
    6: 0.66,
    7: 0.78,
    8: 0.75,
    9: 0.82,
    10: 0.81,
}


def get_apouey_index(categories: ArrayLike, responses: Sequence) -> float:
    number_of_categories = categories[-1]
    if number_of_categories < 3 or number_of_categories > 10:
        raise ValueError(
            "Category out of range. Please use category within range 3-10."
        )

    alpha = ALPHA_LOOKUP_TABLE[number_of_categories]
    proportions_info = info(responses, categories)

    sum_fc_alpha = 0

    for category in range(1, number_of_categories):
        fc = proportions_info["cumulative"][category] / 100
        sum_fc_alpha += abs(fc - 0.5) ** alpha

    apouey_index = 1 - (2**alpha) / categories[-2] * sum_fc_alpha
    return apouey_index
