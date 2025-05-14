from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import select
from src.core import get_session
from src.core.utils import normalize_word
from src.models import Profile, Room, Game, Word, Distance, Hint
from src.schemas import GuessOut, HintOut
from src.auth.dependencies import get_current_user

room_router = APIRouter(tags=["Room"])

@room_router.get("/{room_id}/guess/{guess}", response_model=GuessOut)
def guess_word(room_id: int, guess: str, user: Profile = Depends(get_current_user)):
    guess = normalize_word(guess)

    with get_session() as session:
        room = session.get(Room, room_id)
        if not room or not room.fk_game_id:
            raise HTTPException(status_code=404, detail="Room or game not found")

        game = session.get(Game, room.fk_game_id)
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

        return GuessOut(
            guess=guess,
            distance=dist.distance,
            x=dist.x,
            y=dist.y,
            correct=word_obj.id == game.fk_target_word
        )

@room_router.get("/{room_id}/hint/{hint_number}", response_model=HintOut)
def get_hint(room_id: int, hint_number: int):
    if not (1 <= hint_number <= 10):
        raise HTTPException(status_code=400, detail="Hint number must be between 1 and 10")

    with get_session() as session:
        room = session.get(Room, room_id)
        if not room or not room.fk_game_id:
            raise HTTPException(status_code=404, detail="Room or game not found")

        game = session.get(Game, room.fk_game_id)
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
