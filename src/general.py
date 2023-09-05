import typing

import pandas as pd


def summary(data: typing.Iterable, percentiles_list=None) -> pd.DataFrame:
    """
    Calculates summary statistics of observed levels
    :param percentiles_list: the percentiles to include in the output,
    should fall between 0 and 1
    :param data: list-like or array-like object with numerical data
    :return: pandas DataFrame with statistics
    """
    if percentiles_list is None:
        percentiles_list = [0.25, 0.5, 0.75]
    df = pd.DataFrame(data).describe(percentiles=percentiles_list)
    df.columns = ["summary"]
    return df
