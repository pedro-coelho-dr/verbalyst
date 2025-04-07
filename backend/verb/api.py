from fastapi import FastAPI, HTTPException, Path
from pathlib import Path as FilePath
from pydantic import BaseModel
from verb.config import GAMES_PATH, FIXED_WORD
from functools import lru_cache
import json
import unicodedata
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ========== Permitir frontend local durante desenvolvimento
origins = [
    "http://localhost:9000",  # Quasar dev server
    "http://127.0.0.1:9000",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # ou ["*"] para todos (não recomendado em prod)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ==========

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

@app.get("/verb/guess/{guess}")
def check_guess(
    guess: str = Path(..., description="The word guessed by the player")  # <- agora vai funcionar
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
