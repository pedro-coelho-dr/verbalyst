import random
from verb.core.model import load_model
from verb.core.config import WORD_SELECTION_STRATEGY, FIXED_WORD

def choose_word_of_the_day():
    model = load_model()
    words = list(model.key_to_index.keys())

    if WORD_SELECTION_STRATEGY == "fixed":
        return FIXED_WORD

    elif WORD_SELECTION_STRATEGY == "random":
        return random.choice(words)

    else:
        raise ValueError(f"Unsupported word selection strategy: {WORD_SELECTION_STRATEGY}")
