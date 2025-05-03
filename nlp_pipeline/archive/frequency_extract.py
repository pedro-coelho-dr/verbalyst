TOP_N = 5000
INPUT_PATH = "../data/lemas.totalbr.freq.txt"
OUTPUT_PATH = "../data/top5k-br.txt"

def is_valid_word(word):
    return word.isalpha() and len(word) >= 2  # Ignora pontuação, números, 1 letra só

def extract_top_words():
    words = []
    with open(INPUT_PATH, "r", encoding="latin-1") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) != 2:
                continue
            _, word = parts
            if is_valid_word(word):
                words.append(word.lower())
            if len(words) >= TOP_N:
                break

    with open(OUTPUT_PATH, "w", encoding="utf-8") as out:
        out.write("\n".join(words))
    print(f"{len(words)} palavras salvas em {OUTPUT_PATH}")

if __name__ == "__main__":
    extract_top_words()
