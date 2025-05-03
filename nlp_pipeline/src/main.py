from config import (
    FREQ_PATH, UTF8_DICT_PATH, ASCII_DICT_PATH, MODEL_TXT_PATH, MODEL_OUTPUT_PATH
)
from frequency import extract_top_words
from io_utils import save_log
from normalize import normalize_word
from filters import filter_by_dict, remove_duplicates_normalized
from model_utils import load_word2vec, filter_model_by_vocab

def main():
    print("== VERBALYST: FILTERING MODEL ==")

    print("Extraindo top-N palavras da lista de lemas...")
    top_words = extract_top_words(FREQ_PATH, top_n=10000, min_len=2)

    print("Cruzando com br-utf8.txt...")
    words_in_dict = filter_by_dict(top_words, UTF8_DICT_PATH)

    print("Normalizando palavras e removendo duplicatas...")
    normalized = remove_duplicates_normalized(words_in_dict)

    print("Cruzando com br-sa.txt...")
    final_vocab = filter_by_dict(normalized, ASCII_DICT_PATH)

    print("Carregando modelo Word2Vec original...")
    model = load_word2vec(MODEL_TXT_PATH)

    print("Filtrando modelo...")
    filtered_model, kept_words = filter_model_by_vocab(model, final_vocab)

    print("Salvando modelo final em .kv...")
    filtered_model.save(MODEL_OUTPUT_PATH)

    print("Salvando log de palavras mantidas...")
    save_log(kept_words, "logs/filtered_words.txt")

    print("== FINALIZADO ==")

if __name__ == "__main__":
    main()
