import numpy as np
import typing

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


def get_apouey_index(categories: int, responses: typing.List[int]) -> float:
    if categories < 3 or categories > 10:
        raise AttributeError(
            "Category out of range. Please use category within range 3-10."
        )
    resp_cumulative_proportions = _get_cumulative_proportions(
        _get_proportions(categories, responses)
    )
    sum_fc_alpha = 0
    for category in range(1, categories - 1):
        fc = resp_cumulative_proportions[category]
        sum_fc_alpha += abs(fc - 0.5) ** ALPHA_LOOKUP_TABLE[categories]

    result = 1 - (
            (2 ** ALPHA_LOOKUP_TABLE[categories]) / (categories - 1)
    ) * sum_fc_alpha
    return round(result, 2)


def _get_proportions(categories: int, responses: typing.List[int]) -> dict:
    proportions_dict = {}
    responses_num = len(responses)
    for category in range(1, categories + 1):
        proportions_dict[category] = round(
            responses.count(category) / responses_num, 2)

    return proportions_dict


def _get_cumulative_proportions(proportions_dict: dict) -> dict:
    cumulative_proportions_dict = {}
    proportions_list = list(proportions_dict.values())
    for key, value in proportions_dict.items():
        if key == 3:
            cumulative_proportions_dict[key] = value
        cumulative_proportions_dict[key] = round(
            sum(proportions_list[:key]), 2)
    return cumulative_proportions_dict
