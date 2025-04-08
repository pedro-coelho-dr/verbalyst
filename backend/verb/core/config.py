from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR.parent / "models" / "word2vec_filtered.kv"
GAMES_PATH = BASE_DIR.parent / "games"


WORD_SELECTION_STRATEGY = "fixed"
FIXED_WORD = "semantica"