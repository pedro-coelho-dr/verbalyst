from fastapi import APIRouter, HTTPException
from sqlmodel import select

from src.core import get_session
from src.models import Game, Hint, Word
from src.schemas import HintOut

hint_router = APIRouter(tags=["Hint"])

@hint_router.get("/{game_id}/{hint_number}", response_model=HintOut)
def get_hint(game_id: int, hint_number: int):
    if not (1 <= hint_number <= 10):
        raise HTTPException(status_code=400, detail="Hint number must be between 1 and 10")

    with get_session() as session:
        game = session.get(Game, game_id)
        if not game:
            raise HTTPException(status_code=404, detail="Game not found")

        hints = session.exec(
            select(Hint)
            .where(Hint.fk_target == game.fk_target_word)
            .order_by(Hint.distance.desc())
        ).all()

        if len(hints) < hint_number:
            raise HTTPException(status_code=404, detail="Not enough hints for this game")

        hint = hints[hint_number - 1] 

        word = session.get(Word, hint.fk_word)
        return HintOut(
            word=word.word,
            distance=hint.distance,
            x=hint.x,
            y=hint.y
        )
