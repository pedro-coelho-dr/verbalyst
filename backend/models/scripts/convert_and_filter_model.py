import unicodedata
from gensim.models import KeyedVectors
import numpy as np

# === CONFIGURATION ===
TXT_MODEL_PATH = "word2vec_skip_100.txt"             # Input model (.txt format)
NORMALIZED_VOCAB_PATH = "br-sa.txt"                  # List of allowed words (already accent-free)
OUTPUT_KV_PATH = "word2vec_filtered.kv"   # Output filtered model

# === HELPERS ===
def remove_accents(word: str) -> str:
    return ''.join(
        char for char in unicodedata.normalize('NFKD', word)
        if not unicodedata.combining(char)
    )

def load_reference_vocabulary(path: str) -> set:
    with open(path, "r", encoding="utf-8") as file:
        return set(line.strip().lower() for line in file if line.strip())

# === MAIN PIPELINE ===
def convert_and_filter():
    print("Loading original Word2Vec model from .txt...")
    original_model = KeyedVectors.load_word2vec_format(TXT_MODEL_PATH, binary=False)

    print("Loading normalized reference vocabulary...")
    reference_vocab = load_reference_vocabulary(NORMALIZED_VOCAB_PATH)

    filtered_words = []
    filtered_vectors = []
    normalized_seen = set()
    skipped_count = 0

    print("Filtering and normalizing vocabulary...")
    for original_word in original_model.key_to_index:
        normalized_word = remove_accents(original_word.lower())

        if normalized_word in reference_vocab:
            if normalized_word not in normalized_seen:
                filtered_words.append(normalized_word)
                filtered_vectors.append(original_model[original_word])
                normalized_seen.add(normalized_word)
            else:
                skipped_count += 1  # Already added
        else:
            skipped_count += 1  # Not in reference list

    print(f"Final word count: {len(filtered_words)}")
    print(f"Words removed or duplicated: {skipped_count}")

    print("Saving filtered model to .kv format...")
    filtered_model = KeyedVectors(vector_size=original_model.vector_size)
    filtered_model.add_vectors(filtered_words, np.array(filtered_vectors))
    filtered_model.save(OUTPUT_KV_PATH)

    print(f"Done. Model saved at: {OUTPUT_KV_PATH}")

# === ENTRY POINT ===
if __name__ == "__main__":
    convert_and_filter()
