# intersect_top_vocab.py

TOP_WORDS_PATH = "../data/top5k-br.txt"
UTF8_VOCAB_PATH = "../data/br-utf8.txt"
OUTPUT_PATH = "../data/top5k-br_intersected.txt"

def load_word_list(path):
    with open(path, "r", encoding="utf-8") as f:
        return set(line.strip().lower() for line in f if line.strip())

def main():
    top_words = load_word_list(TOP_WORDS_PATH)
    utf8_vocab = load_word_list(UTF8_VOCAB_PATH)

    intersection = sorted(top_words & utf8_vocab)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(intersection))

    print(f"{len(intersection)} palavras comuns salvas em: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
