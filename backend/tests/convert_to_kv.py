from gensim.models import KeyedVectors
import os

TXT_PATH = os.path.join("..", "models", "word2vec_skip_100.txt")
KV_PATH = os.path.join("..", "models", "word2vec_skip_100.kv")


def main():
    model = KeyedVectors.load_word2vec_format(TXT_PATH, binary=False)
    model.save(KV_PATH)


if __name__ == "__main__":
    main()