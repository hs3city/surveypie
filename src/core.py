from typing import Sequence, Union

from numpy import ndarray
import pandas as pd
from pandas import Index, Series
from pandas.core.arrays import ExtensionArray


def info(ds: Sequence,
         indicators: Union[ExtensionArray, ndarray, Index, Series, Sequence, list, range, None]) -> pd.DataFrame:
    """
    Get basic summary statistics.

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
    freq_counts = pd.value_counts(ds)
    freq_counts.name = 'frequency'
    freq_counts_df = pd.DataFrame(freq_counts)
    freq_counts_df.index.name = 'indicator'

    # Calculate ratio
    total_responses = len(ds)
    freq_counts_df['ratio'] = (freq_counts_df['frequency'] / total_responses) * 100

    # Add all indicators
    summary_df = pd.DataFrame(index=indicators, columns=['frequency', 'ratio'])
    summary_df.index.name = 'indicator'

    # Merge the frequency and percent DataFrames to include 0 counts for missing indicators
    summary_df.update(freq_counts_df, join="left")
    summary_df.fillna(0, inplace=True)

    # Calculate cumulative percent
    summary_df['cumulative'] = summary_df['ratio'].cumsum()

    # Set the last cumulative value to 100
    summary_df.loc[summary_df['cumulative'] > 100, 'cumulative'] = 100

    # Create the final DataFrame
    return summary_df
