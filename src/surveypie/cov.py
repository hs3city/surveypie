from numpy.typing import ArrayLike
import numpy as np


def coeff_of_variation(responses: ArrayLike, weights: ArrayLike = None) -> float:
    """
    Function calculates coefficient of variation, and weighted coefficient
    of variation.

    Parameters
    ----------
    responses : array-like
        Responses as numerical values. The list might be unordered.

    weights : array-like, optional
        Weight applied to each response. The same length as responses array.
        Weights are optional.

    Returns
    -------
    : float
        Coefficient of variation or weighted coefficient of variation
        if weights are provided.
    """

    if weights is None:
        r_mean = np.mean(responses)
        r_std = np.std(responses)

        if r_mean == 0:
            raise ZeroDivisionError(
                "Mean of responses is equal to 0, "
                "which means that division by zero is "
                "requested, cannot proceed!."
            )

        cov = r_std / r_mean
    else:
        w_mean = np.average(responses, weights=weights)
        w_std = np.sqrt(np.cov(responses, aweights=weights, bias=True))

        if w_mean == 0:
            raise ZeroDivisionError(
                "Weighted mean of responses is equal to 0, "
                "which means that division by zero is "
                "requested, cannot proceed!."
            )

        cov = w_std / w_mean

    return cov
