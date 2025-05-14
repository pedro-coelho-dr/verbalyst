from sqlmodel import SQLModel, Field
from typing import Optional

class Profile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    auth_provider: str #  "github"
    auth_sub: str = Field(index=True, unique=True) # ID do GitHub
    username: str # Login do GitHub
    total_score: int = 0
    total_games: int = 0
    total_wins: int = 0
    total_hints_used: int = 0
    total_guesses: int = 0
