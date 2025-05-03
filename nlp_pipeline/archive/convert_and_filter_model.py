import unicodedata
from gensim.models import KeyedVectors
import numpy as np

# === CONFIGURATION ===
MODEL_PATH = "../data/word2vec_skip_100.txt"             # Modelo original (.txt)
VOCAB_PATH = "../data/top5k_br_cleaned.txt"              # Lista normalizada final (sem acentos)
OUTPUT_PATH = "../models/word2vec_final.kv"              # Modelo final reduzido

def remove_accents(word: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize("NFKD", word)
        if not unicodedata.combining(c)
    )

def load_clean_vocab(path: str) -> set:
    with open(path, "r", encoding="utf-8") as f:
        return set(line.strip().lower() for line in f if line.strip())

def main():
    print("Loading Word2Vec model (.txt)...")
    model = KeyedVectors.load_word2vec_format(MODEL_PATH, binary=False)

    print("Loading normalized clean vocabulary...")
    clean_vocab = load_clean_vocab(VOCAB_PATH)

    seen = set()
    words = []
    vectors = []

    print("Filtering model...")
    for word in model.key_to_index:
        normalized = remove_accents(word.lower())

        if normalized in clean_vocab and normalized not in seen:
            words.append(normalized)
            vectors.append(model[word])
            seen.add(normalized)

    print(f"Words kept: {len(words)}")

    print("Saving to binary .kv format...")
    filtered_model = KeyedVectors(vector_size=model.vector_size)
    filtered_model.add_vectors(words, np.array(vectors))
    filtered_model.save(OUTPUT_PATH)

    print(f"Done. Saved at: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
