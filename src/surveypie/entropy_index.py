from surveypie.structure.index_model import BaseIndex


class EntropyIndex(BaseIndex):
    """
    Entropy Index metadata

    Attributes
    ----------
    index : float
        Entropy index.

    name : str = 'Generalized entropy index'

    a : float
        Parameter controlling sensitivity to income levels: large `a` is
        especially sensitivie to existence of large incomes, and small
        `a` is sensitive to small incomes.
        # todo: a == 0 or a == 1 or a > 1 - description

    """

    name: str = "Generalized entropy index"
    a: float = 0
