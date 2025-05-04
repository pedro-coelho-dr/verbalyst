from sqlmodel import SQLModel, Field
from typing import Optional

class Word(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    word: str = Field(index=True, unique=True)
    x: Optional[float] = Field(default=None)
    y: Optional[float] = Field(default=None)