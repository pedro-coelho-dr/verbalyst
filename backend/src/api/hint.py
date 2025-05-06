from fastapi import APIRouter, HTTPException
from sqlmodel import select
from typing import List

from src.core import get_session
from src.models import Game, Hint, Word
from src.schemas import HintOut

router = APIRouter(prefix="/hints", tags=["Hints"])

@router.get("/{game_id}", response_model=List[HintOut])
def get_hints(game_id: int):
    with get_session() as session:
        game = session.get(Game, game_id)
        if not game:
            raise HTTPException(status_code=404, detail="Game not found")

        hints = session.exec(
            select(Hint).where(Hint.fk_target == game.fk_target_word)
        ).all()

        return [
            HintOut(
                word=session.get(Word, hint.fk_word).word,
                distance=hint.distance,
                x=hint.x,
                y=hint.y
            )
            for hint in hints
        ]
