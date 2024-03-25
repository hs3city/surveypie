import pandas as pd
from numpy.typing import ArrayLike
from typing import Sequence


def info(ds: Sequence, indicators: ArrayLike) -> pd.DataFrame:
    """
    Get basic summary statistics about ordinal dataset.

    Parameters
    ----------
    ds : Sequence
        The collection of answers or grades.

    indicators : Ordered Sequence
        The ordered collection of unique answers or grades.

    Returns
    -------
    summary_df : pandas DataFrame
        Summary statistics for an ordinal dataset.
    """

    # Calculate frequency using pandas value_counts()
    freq_counts = pd.Series(ds).value_counts()
    freq_counts.name = "frequency"
    freq_counts_df = pd.DataFrame(freq_counts)
    freq_counts_df.index.name = "indicator"

    # Calculate ratio
    total_responses = len(ds)
    counts_to_total = freq_counts_df["frequency"] / total_responses
    freq_counts_df["ratio %"] = counts_to_total * 100

    # Add all indicators
    summary_df = pd.DataFrame(index=indicators, columns=["frequency", "ratio %"])
    summary_df.index.name = "indicator"

    # Merge the frequency and percent DataFrames
    # to include 0 counts for missing indicators
    summary_df.update(freq_counts_df, join="left")
    summary_df.fillna(0, inplace=True)

    # Calculate cumulative percent
    summary_df["cumulative"] = summary_df["ratio %"].cumsum() / 100

    # Set the last cumulative value to 100
    summary_df.loc[summary_df["cumulative"] > 1, "cumulative"] = 1

    # Create the final DataFrame
    return summary_df


def summary(data: ArrayLike, percentiles=None) -> pd.DataFrame:
    """
    Calculates summary statistics of observed levels
    :param percentiles: the percentiles to include in the output,
    should fall between 0 and 1
    :param data: list-like or array-like object with numerical data
    :return: pandas DataFrame with statistics
    """
    if percentiles is None:
        percentiles = [0.25, 0.5, 0.75]
    df = pd.DataFrame(data).describe(percentiles=percentiles)
    df.columns = ["summary"]
    return df
