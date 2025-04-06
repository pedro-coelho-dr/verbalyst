import unicodedata
from gensim.models import KeyedVectors

def remover_acentos(palavra):
    return ''.join(c for c in unicodedata.normalize('NFKD', palavra) if not unicodedata.combining(c))

def carregar_vocab_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return set(linha.strip() for linha in f if linha.strip())

def filtrar_modelo(path_modelo, path_vocab_txt, path_saida):
    print("Carregando modelo...")
    model = KeyedVectors.load(path_modelo, mmap='r')

    print("Carregando vocabulário de referência...")
    vocab_validas = carregar_vocab_txt(path_vocab_txt)

    print(f"Palavras no vocabulário de referência: {len(vocab_validas)}")

    palavras_filtradas = [
        palavra for palavra in model.key_to_index
        if remover_acentos(palavra.lower()) in vocab_validas
    ]

    print(f"Palavras mantidas após filtro: {len(palavras_filtradas)}")

    novo_modelo = model.__class__(vector_size=model.vector_size)
    novo_modelo.add_vectors(palavras_filtradas, [model[palavra] for palavra in palavras_filtradas])

    print("Salvando novo modelo filtrado...")
    novo_modelo.save(path_saida)
    print(f"Modelo salvo em: {path_saida}")

if __name__ == "__main__":
    filtrar_modelo(
        "word2vec_skip_100.kv",
        "br-sa.txt",
        "word2vec_filtrado.kv"
    )
