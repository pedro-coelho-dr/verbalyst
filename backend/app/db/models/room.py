from sqlmodel import SQLModel, Field
from typing import Optional

class Room(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: int = Field(index=True, unique=True)
    status: str = "active"
