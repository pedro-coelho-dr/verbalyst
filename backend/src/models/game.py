from sqlmodel import SQLModel, Field
from typing import Optional

class Game(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fk_target_word: int = Field(foreign_key="word.id")