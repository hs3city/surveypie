import pandas as pd
from numpy.typing import ArrayLike


def info(responses: ArrayLike, indicators: ArrayLike) -> pd.DataFrame:
    """
    Get basic summary statistics about ordinal dataset.

    Parameters
    ----------
    responses : ArrayLike
        The collection of answers or grades.

    indicators : ArrayLike
        The ordered collection of possible answers or grades.

    Returns
    -------
    summary_df : pandas DataFrame
        Summary statistics for an ordinal dataset.
    """

    # Calculate frequency using pandas value_counts()
    freq_counts = pd.Series(responses).value_counts()
    freq_counts.name = "frequency"
    freq_counts_df = pd.DataFrame(freq_counts)
    freq_counts_df.index.name = "indicator"

    # Calculate ratio
    total_responses = len(responses)
    counts_to_total = freq_counts_df["frequency"] / total_responses
    freq_counts_df["ratio %"] = counts_to_total * 100.0

    # Add all indicators
    summary_df = pd.DataFrame(index=indicators)
    summary_df.index.name = "indicator"

    # Merge the frequency and percent DataFrames
    # to include 0 counts for missing indicators
    summary_df = summary_df.join(freq_counts_df, how="left")
    summary_df.fillna(0.0, inplace=True)

    # Calculate cumulative percent
    summary_df["cumulative"] = summary_df["ratio %"].cumsum() / 100.0

    # Set the last cumulative value to 100
    summary_df.loc[summary_df["cumulative"] > 1.0, "cumulative"] = 1.0

    # Create the final DataFrame
    return summary_df


def summary(responses: ArrayLike, percentiles=None) -> pd.DataFrame:
    """
    Calculates summary statistics of observed levels

    Parameters
    ----------
    responses : ArrayLike
        The collection of numerical responses.

    percentiles : ArrayLike, optional
        The percentiles to include in the output, every percentile should
        fall between 0 and 1

    Returns
    -------
    df : DataFrame

    """
    if percentiles is None:
        percentiles = [0.25, 0.5, 0.75]
    df = pd.DataFrame(responses).describe(percentiles=percentiles)
    df.columns = ["summary"]
    return df
