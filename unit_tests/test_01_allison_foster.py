import random

from src import allison_foster
from src.allison_foster import af_index, AllisonFosterIndex


def test_measures_calculation():
    example_data = random.sample(range(1, 1000), 500)
    result = af_index(example_data)
    assert isinstance(result, AllisonFosterIndex)
    assert isinstance(result.index, float)
    assert isinstance(result.u_l, float)
    assert isinstance(result.u_h, float)


def test_on_example():
    dataset = [1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5]

    # estimated_median = 3
    estimated_u_l = 7 / 6
    estimated_u_h = 33 / 7
    estimated_index = estimated_u_h - estimated_u_l
    allison_foster_index = af_index(dataset)
    assert estimated_u_l == allison_foster_index.u_l
    assert estimated_u_h == allison_foster_index.u_h
    assert estimated_index == allison_foster_index.index
