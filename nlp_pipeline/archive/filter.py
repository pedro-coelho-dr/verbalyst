from gensim.models import KeyedVectors
import numpy as np
from typing import Set, Tuple, List

def load_vocabulary(path: str, min_length: int = 2) -> Set[str]:
    with open(path, "r", encoding="utf-8") as f:
        return {
            word.strip()
            for word in f
            if len(word.strip()) >= min_length
        }

def filter_word_vectors(model_path: str, vocabulary: Set[str]) -> Tuple[List[str], np.ndarray, int]:
    model = KeyedVectors.load_word2vec_format(model_path, binary=False)
    filtered_words = []
    filtered_vectors = []

    for word in model.key_to_index:
        if word in vocabulary:
            filtered_words.append(word)
            filtered_vectors.append(model[word])

    return filtered_words, np.array(filtered_vectors), model.vector_size

def save_filtered_model(words: List[str], vectors: np.ndarray, vector_size: int, output_path: str) -> None:
    filtered_model = KeyedVectors(vector_size=vector_size)
    filtered_model.add_vectors(words, vectors)
    filtered_model.save(output_path)
