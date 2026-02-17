import random
import numpy as np
import pytest

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

        highest = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
        lowest = np.ones(10) * cat  # lowest dispersion because all answers
        # are in a single group and zero in other groups...
        # highest concentration

        d_low = bl_index(categories=categories, responses=lowest)
        d_high = bl_index(categories=categories, responses=highest)

        assert d_low.index < d_high.index


def test_range():
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
        assert result.index >= 0
        assert result.index_sqrt <= 1
        assert result.index_sqrt >= 0


def test_based_on_table_1_example_from_publication():
    """
    Blair J, Lacy M G. (2000): Statistics of ordinal variation,
    Sociological Methods and Research 28(251);251-280

    TABLE 1

    """

    categories = [1, 2, 3, 4]
    excellent = 153 * [1]
    good = 208 * [2]
    fair = 74 * [3]
    poor = 23 * [4]

    responses = excellent + good + fair + poor

    result = bl_index(categories=categories,
                        responses=responses)
    # expected
    l2 = 0.417
    index = 0.583

    assert l2 == pytest.approx(result.l2_index, 3)
    assert index == pytest.approx(result.index, 3)


def test_based_on_table_2_example_A_from_publication():
    """
    Blair J, Lacy M G. (2000): Statistics of ordinal variation,
    Sociological Methods and Research 28(251);251-280

    TABLE 2

    """

    categories = [1, 2, 3, 4]
    excellent = 60 * [1]
    good = []
    fair = 20 * [3]
    poor = 20 * [4]

    responses = excellent + good + fair + poor

    result = bl_index(categories=categories,
                      responses=responses)
    # expected
    l2 = 0.120

    assert l2 == pytest.approx(result.l2_index, 3)


def test_based_on_table_2_example_B_from_publication():
    """
    Blair J, Lacy M G. (2000): Statistics of ordinal variation,
    Sociological Methods and Research 28(251);251-280

    TABLE 2

    """

    categories = [1, 2, 3, 4]
    excellent = 50 * [1]
    good = []
    fair = 30 * [3]
    poor = 20 * [4]

    responses = excellent + good + fair + poor

    result = bl_index(categories=categories,
                      responses=responses)
    # expected
    l2 = 0.147

    assert l2 == pytest.approx(result.l2_index, 3)


def test_based_on_table_2_example_F_from_publication():
    """
    Blair J, Lacy M G. (2000): Statistics of ordinal variation,
    Sociological Methods and Research 28(251);251-280

    TABLE 2

    """

    categories = [1, 2, 3, 4]
    excellent = 10 * [1]
    good = []
    fair = 70 * [3]
    poor = 20 * [4]

    responses = excellent + good + fair + poor

    result = bl_index(categories=categories,
                      responses=responses)
    # expected
    l2 = 0.787

    assert l2 == pytest.approx(result.l2_index, 3)
