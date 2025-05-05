from sqlmodel import SQLModel, Field
from typing import Optional

class Coordinates(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fk_word: int = Field(foreign_key="word.id")
    fk_target: int = Field(foreign_key="word.id")  # palavra-alvo
    x: float
    y: float
