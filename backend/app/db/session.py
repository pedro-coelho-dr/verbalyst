from sqlmodel import SQLModel, create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    from app.db.models import profile, word, room, game, player, guess, wordscore
    SQLModel.metadata.create_all(engine)