from verb.word_bank import escolher_palavra_do_dia
from verb.generator import gerar_jogo

if __name__ == "__main__":
    palavra = escolher_palavra_do_dia()
    gerar_jogo(palavra, f"jogo_{palavra}.json")