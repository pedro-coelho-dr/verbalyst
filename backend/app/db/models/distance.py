from sqlmodel import SQLModel, Field
from typing import Optional

class Distance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fk_word: int = Field(foreign_key="word.id")
    fk_target: int = Field(foreign_key="word.id")
    distance: int

