import random
import numpy as np

from surveypie.blair_lacy_index import bl_index, BlairLacyIndex


def test_random():
    categories = list(range(1, 10))
    example_data = random.choices(categories, k=500)
    result = bl_index(categories=categories, responses=example_data)

    assert isinstance(result, BlairLacyIndex)
    assert isinstance(result.index, float)
    assert isinstance(result.index_sqrt, float)
    assert isinstance(result.min_dispersion, float)
    assert result.n_classes == len(categories)
    assert result.name == "Blair and Lacy Index"


def test_dispersion():
    """
    Test with the same answers (under ``lowest`` variable) is performed for
    each category in a for loop.
    """

    categories = [1, 2, 3]

    for cat in categories:
        lowest = np.ones(10) * cat
        middle = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
        highest = [1, 1, 1, 1, 1, 3, 3, 3, 3, 3]

        d_low = bl_index(categories=categories, responses=lowest)
        d_mid = bl_index(categories=categories, responses=middle)
        d_high = bl_index(categories=categories, responses=highest)

        assert d_low.index < d_mid.index
        assert d_mid.index < d_high.index


def test_not_greater_than_1():
    categories_3 = [1, 2, 3]
    categories_5 = list(range(1, 6))
    categories_10 = list(range(1, 11))

    example_data_3 = random.choices(categories_3, k=5000)
    example_data_5 = random.choices(categories_5, k=5000)
    example_data_10 = random.choices(categories_10, k=5000)

    cats = [categories_3, categories_5, categories_10]
    datasets = [example_data_3, example_data_5, example_data_10]

    for idx in range(len(datasets)):
        result = bl_index(
            categories=cats[idx],
            responses=datasets[idx]
        )

        assert result.index <= 1
