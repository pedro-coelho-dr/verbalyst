from sqlmodel import SQLModel, Field
from typing import Optional

class Hint(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fk_target: int = Field(foreign_key="word.id")
    fk_word: int = Field(foreign_key="word.id")
    fk_room_id: Optional[int] = Field(default=None, foreign_key="room.id")
    distance: int
    x: float
    y: float
    