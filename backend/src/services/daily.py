from datetime import date
from sqlmodel import select
from src.core import get_session
from src.models import Game

def get_daily_game_id() -> int:
    today = date.today()

    with get_session() as session:
        games = session.exec(select(Game).order_by(Game.id)).all()
        if not games:
            raise Exception("No games found in database")

        day_of_year = (today - date(today.year, 1, 1)).days
        index = day_of_year % len(games)

        return games[index].id
