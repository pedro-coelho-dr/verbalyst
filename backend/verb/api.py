from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from verb.config import GAMES_PATH, FIXED_WORD
from pathlib import Path
from functools import lru_cache
import json
import unicodedata

app = FastAPI()

def remove_accents(word: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFKD', word)
        if not unicodedata.combining(c)
    )

@lru_cache(maxsize=1)
def load_game_from_disk(word: str):
    filename = f"game_{word}.json"
    filepath = GAMES_PATH / filename

    if not filepath.exists():
        raise HTTPException(status_code=404, detail=f"Game file '{filename}' not found.")

    with open(filepath, encoding="utf-8") as f:
        return json.load(f)

@app.get("/guess")
def check_guess(
    guess: str = Query(..., description="The word guessed by the player")
):
    normalized_guess = remove_accents(guess.strip().lower())
    target_word = remove_accents(FIXED_WORD.strip().lower())

    if normalized_guess == target_word:
        return {
            "guess": normalized_guess,
            "score": 100,
            "correct": True
        }

    game_data = load_game_from_disk(FIXED_WORD)
    ranking = game_data["ranking"]

    if normalized_guess not in ranking:
        raise HTTPException(status_code=404, detail=f"Word '{guess}' not found in game vocabulary.")

    return {
        "guess": normalized_guess,
        "score": ranking[normalized_guess],
        "correct": normalized_guess == target_word
    }
