from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Player(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fk_game_id: int = Field(foreign_key="game.id")
    fk_profile_id: int = Field(foreign_key="profile.id")
    hints_used: int = 0
    completed: bool = False
    completed_at: Optional[datetime]
    score_gained: int = 0
    guesses_count: int = 0
