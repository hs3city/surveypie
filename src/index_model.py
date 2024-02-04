from pydantic import BaseModel


class BaseIndex(BaseModel):
    """Represents base index"""
    index: float
    name: str
