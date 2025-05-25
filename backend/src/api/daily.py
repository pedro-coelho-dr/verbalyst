from fastapi import APIRouter, HTTPException
from sqlmodel import select
from src.core import get_session
from src.models import Game, Hint, Word, Distance
from src.schemas import GuessOut, HintOut
from src.services.daily import get_daily_game_id
from src.core.utils import normalize_word

daily_router = APIRouter(tags=["Daily"])

@daily_router.get("/game")
def get_daily_game():
    game_id = get_daily_game_id()
    return {"game_id": game_id}


@daily_router.get("/hint/{hint_number}", response_model=HintOut)
def get_hint(hint_number: int):
    if not (1 <= hint_number <= 10):
        raise HTTPException(status_code=400, detail="Hint number must be between 1 and 10")

    with get_session() as session:
        game_id = get_daily_game_id()
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


@daily_router.get("/guess/{guess}", response_model=GuessOut)
def guess_word(guess: str):
    guess = normalize_word(guess)

    with get_session() as session:
        game_id = get_daily_game_id()
        game = session.get(Game, game_id)
        if not game:
            raise HTTPException(status_code=404, detail="Game not found")

        word_obj = session.exec(select(Word).where(Word.word == guess)).first()
        if not word_obj:
            raise HTTPException(status_code=404, detail="Word not found")

        if word_obj.id == game.fk_target_word:
            return GuessOut(
                guess=guess,
                distance=0,
                x=0.0,
                y=0.0,
                correct=True
            )

        dist = session.exec(
            select(Distance)
            .where(Distance.fk_target == game.fk_target_word)
            .where(Distance.fk_word == word_obj.id)
        ).first()

        if not dist:
            raise HTTPException(status_code=404, detail="Word not in this game")

        return GuessOut(
            guess=guess,
            distance=dist.distance,
            x=dist.x,
            y=dist.y,
            correct=False
        )
