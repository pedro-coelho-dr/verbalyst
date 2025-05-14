from fastapi import APIRouter, HTTPException
from sqlmodel import select

from src.core import get_session
from src.core.utils import normalize_word
from src.models import Game, Word, Distance
from src.schemas import GuessOut

guess_router = APIRouter(tags=["Guess"])

@guess_router.get("/{game_id}/{guess}", response_model=GuessOut)
def guess_word(game_id: int, guess: str):
    guess = normalize_word(guess)

    with get_session() as session:
        game = session.get(Game, game_id)
        if not game:
            raise HTTPException(status_code=404, detail="Game not found")

        word_obj = session.exec(select(Word).where(Word.word == guess)).first()
        if not word_obj:
            raise HTTPException(status_code=404, detail="Word not found")

        dist = session.exec(
            select(Distance)
            .where(Distance.fk_target == game.fk_target_word)
            .where(Distance.fk_word == word_obj.id)
        ).first()

        if not dist:
            raise HTTPException(status_code=404, detail="Word not in this game")

        score = max(0.0, 100 - dist.distance / 100)

        return GuessOut(
            guess=guess,
            distance=dist.distance,
            x=dist.x,
            y=dist.y,
            correct=word_obj.id == game.fk_target_word
        )
