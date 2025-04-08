from verb.core.word_bank import choose_word_of_the_day
from verb.game.generator import generate_game
from verb.core.config import GAMES_PATH

if __name__ == "__main__":
    word = choose_word_of_the_day()

    existing = [int(f.stem) for f in GAMES_PATH.glob("*.json") if f.stem.isdigit()]
    next_id = max(existing, default=0) + 1

    generate_game(word, next_id)
    print(f"Generated game #{next_id} for word: {word}")
