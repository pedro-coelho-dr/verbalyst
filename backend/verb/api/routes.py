from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from functools import lru_cache
from typing import Dict
import json
import unicodedata

from verb.core.config import GAMES_PATH


app = FastAPI(title="Verbalyst API")

# ========= CORS (Dev only) ========= #
origins = [
    "http://localhost:9000",
    "http://127.0.0.1:9000",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def remove_accents(word: str) -> str:
    """Remove acentos e normaliza para minúsculas."""
    return ''.join(
        c for c in unicodedata.normalize('NFKD', word.lower().strip())
        if not unicodedata.combining(c)
    )


@lru_cache(maxsize=10)
def load_game(game_id: int) -> Dict:
    """Carrega o arquivo JSON do jogo."""
    filepath = GAMES_PATH / f"{game_id}.json"

    if not filepath.exists():
        raise HTTPException(status_code=404, detail=f"Jogo {game_id} não encontrado.")

    with open(filepath, encoding="utf-8") as f:
        return json.load(f)


# ========= Rotas ========= #
@app.get("/verb/guess/{game_id}/{guess}")
def check_guess(
    game_id: int = Path(..., description="ID numérico do jogo"),
    guess: str = Path(..., description="Palavra tentada")
):
    try:
        game = load_game(game_id)
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={"status": "error", "detail": e.detail}
        )

    target_word = remove_accents(game.get("target_word", ""))
    normalized_guess = remove_accents(guess)

    # Palavra correta
    if normalized_guess == target_word:
        return {
            "status": "success",
            "guess": normalized_guess,
            "score": 100,
            "correct": True
        }

    # Palavra presente no ranking
    ranking = game.get("ranking", {})
    score = ranking.get(normalized_guess)

    if score is not None:
        return {
            "status": "success",
            "guess": normalized_guess,
            "score": score,
            "correct": False
        }

    # Palavra desconhecida
    return JSONResponse(
        status_code=404,
        content={
            "status": "warning",
            "detail": f"A palavra '{guess}' não está no vocabulário deste jogo."
        }
    )
