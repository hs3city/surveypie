import numpy as np
from typing import Sequence
from src.core import info, IND_TYPES

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


def get_apouey_index(categories: IND_TYPES, responses: Sequence) -> float:
    number_of_categories = len(categories)
    if number_of_categories < 3 or number_of_categories > 10:
        raise ValueError(
            "Category out of range. Please use category within range 3-10."
        )

    alpha = ALPHA_LOOKUP_TABLE[number_of_categories]
    proportions_info = info(responses, categories)

    sum_fc_alpha = 0

    for category in range(1, len(categories) - 1):
        fc = proportions_info["cumulative"][category] / 100
        sum_fc_alpha += abs(fc - 0.5) ** alpha

    apouey_index = 1 - (2**alpha) / (len(categories) - 1) * sum_fc_alpha
    return apouey_index


if __name__ == "__main__":
    INDICATORS = [1, 2, 3, 4, 5]

    DS = []
    DS.extend(10 * [1])
    DS.extend(10 * [2])
    DS.extend(10 * [3])
    DS.extend(5 * [4])
    DS.extend(15 * [5])
    RESULT = info(DS, INDICATORS)

    print(RESULT)

    print(get_apouey_index(INDICATORS, DS))
