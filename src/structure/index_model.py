from typing import Optional

from pydantic import BaseModel


class BaseIndex(BaseModel):
    """Represents base index"""

    index: float
    name: str
    n_classes: Optional[int] = None
