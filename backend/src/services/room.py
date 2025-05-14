from datetime import date
from sqlmodel import select, Session

from src.models import Room, Game
from src.core import get_session


def get_or_create_daily_room(profile_id: int, db: Session = None) -> Room:
    close_session = False
    if db is None:
        db = get_session()
        close_session = True

    try:
        today = date.today()
        existing_room = db.exec(
            select(Room)
            .where(Room.owner_id == profile_id)
            .where(Room.created_at == today)
        ).first()

        if existing_room:
            return existing_room

        all_games = db.exec(select(Game).order_by(Game.id)).all()
        if not all_games:
            raise Exception("No games found in database")

        index = (today - date(today.year, 1, 1)).days % len(all_games)
        game = all_games[index]

        room = Room(owner_id=profile_id, fk_game_id=game.id, created_at=today)
        db.add(room)
        db.commit()
        db.refresh(room)
        return room
    finally:
        if close_session:
            db.close()


def get_or_create_room_by_game(profile_id: int, game_id: int, db: Session = None) -> Room:
    close_session = False
    if db is None:
        db = get_session()
        close_session = True

    try:
        existing_room = db.exec(
            select(Room)
            .where(Room.owner_id == profile_id)
            .where(Room.fk_game_id == game_id)
        ).first()

        if existing_room:
            return existing_room

        game = db.get(Game, game_id)
        if not game:
            raise ValueError("Game not found")

        room = Room(owner_id=profile_id, fk_game_id=game_id, created_at=date.today())
        db.add(room)
        db.commit()
        db.refresh(room)
        return room
    finally:
        if close_session:
            db.close()
