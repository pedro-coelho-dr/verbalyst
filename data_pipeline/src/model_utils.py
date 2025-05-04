from gensim.models import KeyedVectors
import numpy as np

def load_word2vec(path: str) -> KeyedVectors:
    return KeyedVectors.load_word2vec_format(path, binary=False)

def filter_model_by_vocab(model: KeyedVectors, vocab: set[str]):
    new_words = []
    new_vectors = []
    added = set()

    for word in model.key_to_index:
        norm = word.lower()
        if norm not in vocab or norm in added:
            continue
        new_words.append(norm)
        new_vectors.append(model[word])
        added.add(norm)

    filtered = KeyedVectors(vector_size=model.vector_size)
    filtered.add_vectors(new_words, np.array(new_vectors))
    return filtered, new_words
