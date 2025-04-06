from verb.word_bank import choose_word_of_the_day
from verb.generator import generate_game

if __name__ == "__main__":
    word = choose_word_of_the_day()
    generate_game(word, f"game_{word}.json")
    print(f"Generated game for word: {word}")   