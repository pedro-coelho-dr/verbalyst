from gensim.models import KeyedVectors

def exportar_vocab(path_modelo, path_saida="vocabulario.txt"):
    model = KeyedVectors.load(path_modelo, mmap='r')
    vocab = model.key_to_index.keys()

    with open(path_saida, "w", encoding="utf-8") as f:
        for palavra in vocab:
            f.write(palavra + "\n")

    print(f"Exportado {len(vocab)} palavras para {path_saida}")

if __name__ == "__main__":
    exportar_vocab("../models/word2vec_filtered.kv")
