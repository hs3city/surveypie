from numpy.typing import ArrayLike
import numpy as np

from surveypie.structure.index_model import BaseIndex


class RobinHoodIndex(BaseIndex):
    """
    Robin Hood / Hoover / Schutz index metadata

    Attributes
    ----------
    index : float
        Robin Hood Index.

    name : str = 'Robin Hood Index'

    """

    name: str = "Robin Hood Index"


def robin_hood_index(data: ArrayLike) -> RobinHoodIndex:
    """
    Robin Hood / Hoover / Schutz index calculation.

    Parameters
    ----------
    data : ArrayLike
        Vector with data.

    Returns
    -------
    : RobinHoodIndex

    References
    ----------
    1. Edgar Malone Hoover Jr. (1936) The Measurement of Industrial
       Localization, Review of Economics and Statistics, 18, No. 162–71
    2. Edgar Malone Hoover Jr. (1984) An Introduction to Regional Economics,
       1984, ISBN 0-07-554440-7
    """

    if np.min(data) < 0:
        raise ValueError(
            "Negative values passed into input data array, remove those "
            "or shift values to get the meaningful results of Robin "
            "Hood Index."
        )

    m = np.mean(data)
    h_index = 0.5 * (np.sum(np.abs(data - m)) / np.sum(data))

    return RobinHoodIndex(index=h_index)
