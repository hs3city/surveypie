import pandas as pd

from src.general import summary


def test_on_example():
    dataset = [2, 1, 4, 3, 1, 5, 3, 3, 4, 2, 1,
               1, 3, 3, 4, 5, 5, 4, 3, 2, 2, 1, 2, 1]
    summary_stats = summary(dataset)
    column_name = 'summary'

    assert isinstance(summary_stats, pd.DataFrame)
    assert summary_stats.loc["count", column_name] == len(dataset)
    assert summary_stats.loc["min", column_name] == 1
    assert summary_stats.loc["max", column_name] == 5
    assert round(summary_stats.loc["mean", column_name]) == sum(dataset) \
           / len(dataset)
    assert round(summary_stats.loc["std", column_name], 2) == 1.37
    assert round(summary_stats.loc["25%", column_name], 2) == 1.75
    assert round(summary_stats.loc["50%", column_name], 2) == 3.00
    assert round(summary_stats.loc["75%", column_name], 2) == 4.00
