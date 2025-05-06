from sqlmodel import SQLModel
from app.core.database import engine
from app.models import Profile, Word, Room, Game, Player, Guess, Distance, Hint

def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)
    print("[DONE] Database schema created.")

if __name__ == "__main__":
    create_db_and_tables()
