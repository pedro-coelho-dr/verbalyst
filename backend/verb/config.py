from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "word2vec_filtered.kv"
GAMES_PATH = BASE_DIR / "games"

# Word selection strategy: "fixed", "random", "daily", etc.
WORD_SELECTION_STRATEGY = "fixed"
FIXED_WORD = "felicidade"