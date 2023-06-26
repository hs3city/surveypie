import random

import allison_foster
from allison_foster import AllisonFosterMeasures


def test_measures_calculation():
    example_data = random.sample(range(1, 1000), 500)
    result = allison_foster.compute_measures(example_data)
    assert isinstance(result, AllisonFosterMeasures)
    assert isinstance(result.index, float)
    assert isinstance(result.mean_l, float)
    assert isinstance(result.mean_h, float)