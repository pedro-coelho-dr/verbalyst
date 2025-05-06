from sqlmodel import SQLModel, Field
from typing import Optional

class Guess(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fk_player_id: int = Field(foreign_key="player.id")
    guess: str
    distance: int
    x: float
    y: float
