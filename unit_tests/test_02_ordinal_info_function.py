import numpy as np
import pandas as pd

from src.core import info


INDICATORS = ['not satisfied', 'ok', 'excellent', 'test']

DS = []
DS.extend(3 * ['not satisfied'])
DS.extend(10 * ['ok'])
DS.extend(35 * ['excellent'])
RESULT = info(DS, INDICATORS)


def test_dtype():
    assert isinstance(RESULT, pd.DataFrame)


def test_index_ordering():
    for idx, x in enumerate(RESULT.index.values):
        assert x == INDICATORS[idx]


def test_columns():
    expected_columns = {'frequency', 'ratio', 'cumulative'}
    assert expected_columns == set(RESULT.columns)


def test_ratio():
    ratios = RESULT['ratio'].values
    assert np.alltrue(ratios >= 0)
    assert np.alltrue(ratios <= 100)


def test_cumulative():
    cumsum = RESULT['cumulative'].values
    previous_val = 0
    for x in cumsum:
        assert x >= 0
        assert x <= 100
        assert x >= previous_val
        previous_val = x


def test_range():
    values = np.random.randint(1, 6, 200)
    indicators = range(1, 6, 1)
    range_result = info(values, indicators)
    assert not range_result.isna().any().any()
