"""
Abul Naga and Yalcin indexes implementation.

Author: Szymon Moliński (@SimonMolinsky)

Version: 1.0

Last Revision: 2024-02-25

Contributors:
  -

Tutorials:
  -
"""
import numpy as np
from numpy.typing import ArrayLike
from pydantic import field_validator

from src.core import info
from src.structure.index_model import BaseIndex


class AbulNagaYalcinIndex(BaseIndex):
    """
    Abul Naga and Yalcin Indexes metadata

    Attributes
    ----------
    index : float
        Allison-Foster index.

    name : str = 'Abul Naga & Yalcin Index'

    alpha : float, >= 1
        Controls the weight given to inequalities below the median.

    beta : float, >= 1
        Controls the weight given to inequalities above the median.
    """

    alpha: float
    beta: float
    name: str = "Abul Naga & Yalcin Index"

    @field_validator("alpha", "beta")
    @classmethod
    def greater_or_equal_one(cls, v: float) -> float:
        if v < 1:
            raise ValueError(
                'Parameters "alpha" and "beta" must be greater' "or equal to 1"
            )
        return v


def any_index(
    categories: ArrayLike, responses: ArrayLike, alpha=1.0, beta=1.0
) -> AbulNagaYalcinIndex:
    """
    Abul Naga & Yalcin index.

    Parameters
    ----------
    categories : array
        Ordered list of possible categories.

    responses : array
        Dataset with ordinal-scale values used for index computation.

    alpha : float, default = 1
        Parameter used for index weighting. Must be greater or equal to 1.
        See Notes to learn more about this parameter.

    beta : float, default = 1
        Parameter used for index weighting. Must be greater or equal to 1.
        See Notes to learn more about this parameter.

    Returns
    -------
    index : AbulNagaYalcinIndex

    Notes
    -----
    With ``alpha`` == ``beta`` inequality is at a minimum when everyone is in
    the same category, and at a maximum when half of the population lies in
    the lowest category and half in the highest category.
    Different calibrations of the parameters and allow the researcher to
    give different weights to inequalities above and below the median of
    the responsiveness distribution -
    for higher values of ``alpha`` (``beta``), less weight is given to
    inequalities below (above) the median.

    References
    ----------
    [1] Abul Naga RH, Yalcin T. Inequality measurement for ordered response
    health data. J Health Econ. 2008 Dec;27(6):1614-25.
    doi: 10.1016/j.jhealeco.2008.07.015. Epub 2008 Aug 19. PMID: 18838185.

    [2] Andrew M. Jones, Nigel Rice, Silvana Robone, Pedro Rosa Dias.
    Inequality and Polarisation in Health Systems’ Responsiveness:
    A Cross- Country Analysis. HEDG Working Paper 10/27, October 2010.
    URL: https://www.york.ac.uk/media/economics/documents/herc/wp/10_27.pdf
    """

    n_categories = len(categories)
    m = int(np.median(responses))
    c = n_categories + 1 - m

    exp_alpha = 0.5**alpha
    exp_beta = 0.5**beta

    k_a_b = (m - 1) * exp_alpha - (1 - (n_categories - m) * exp_beta)

    ds = info(ds=responses, indicators=categories)

    ds = ds["cumulative"]
    p_alpha = ds[ds.index < m] / 100
    p_beta = ds[ds.index >= m] / 100

    # below median
    p_alpha_alpha = p_alpha**alpha
    p_a = np.sum(p_alpha_alpha)

    # above and equal to median
    p_beta_beta = p_beta**beta
    p_b = np.sum(p_beta_beta)

    index = (p_a - p_b + c) / (k_a_b + c)

    return AbulNagaYalcinIndex(
        index=index, alpha=alpha, beta=beta, n_classes=n_categories
    )
