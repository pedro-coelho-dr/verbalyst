from sqlmodel import SQLModel, create_engine
import os

from app.db.models import (
    Profile, Word, Room, Game, Player, Guess,
    Distance, Coordinates, Hint
)

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
