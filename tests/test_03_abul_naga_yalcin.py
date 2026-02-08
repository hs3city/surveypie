import random

import numpy as np

from math import isclose

from surveypie.abul_naga_yalcin_index import any_index, AbulNagaYalcinIndex


def test_random():
    categories = list(range(1, 10))
    example_data = random.choices(categories, k=500)
    result = any_index(categories=categories, responses=example_data)

    assert isinstance(result, AbulNagaYalcinIndex)
    assert isinstance(result.index, float)
    assert isinstance(result.alpha, float)
    assert isinstance(result.beta, float)
    assert result.name == "Abul Naga & Yalcin Index"


def test_lowest_vs_highest():
    """
    Test with the same answers (under ``lowest`` variable) is performed for
    each category in a for loop.
    """

    categories = [1, 2, 3]

    for cat in categories:
        lowest = np.ones(10) * cat
        middle = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
        highest = [1, 1, 1, 1, 1, 3, 3, 3, 3, 3]

        res_low = any_index(categories=categories, responses=lowest)

        res_mid = any_index(categories=categories, responses=middle)

        res_high = any_index(categories=categories, responses=highest)

        assert res_low.index < res_mid.index
        assert res_mid.index < res_high.index


def test_weighted_alpha_and_beta():
    """
    We can put additional weight for responses below or above the median using
    ``alpha`` and ``beta`` parameters.

    When ``alpha`` < ``beta`` --- greater weight is given for responses below
    the median.

    When ``alpha`` > ``beta`` --- greater weight is given for responses above
    the median.
    """
    low_param = 1
    high_param = 4

    categories = [1, 2, 3]
    responses = [1, 1, 1, 2, 2]

    res_below_more_important = any_index(
        categories=categories,
        responses=responses,
        alpha=low_param,
        beta=high_param,
    )

    res_above_more_important = any_index(
        categories=categories,
        responses=responses,
        alpha=high_param,
        beta=low_param,
    )

    assert res_below_more_important.index != res_above_more_important.index


def test_not_greater_than_1():
    categories_3 = [1, 2, 3]
    categories_5 = list(range(1, 6))
    categories_10 = list(range(1, 11))

    example_data_3 = random.choices(categories_3, k=5000)
    example_data_5 = random.choices(categories_5, k=5000)
    example_data_10 = random.choices(categories_10, k=5000)

    parameters = [1, 2, 4, 100, 10**6]

    cats = [categories_3, categories_5, categories_10]
    datasets = [example_data_3, example_data_5, example_data_10]

    for idx in range(len(datasets)):
        for param_a in parameters:
            for param_b in parameters:
                result = any_index(
                    categories=cats[idx],
                    responses=datasets[idx],
                    alpha=param_a,
                    beta=param_b,
                )

                if result.index > 1:
                    assert isclose(result.index, 1)
