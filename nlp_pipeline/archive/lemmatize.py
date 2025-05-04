import spacy

INPUT_PATH = "../data/top5k-br_intersected.txt"
OUTPUT_PATH = "../data/top5k-br_lemmatized.txt"

print("Carregando modelo spaCy...")
nlp = spacy.load("pt_core_news_sm", disable=["parser", "ner", "senter"])

def get_lemma(word: str) -> str:
    doc = nlp(word.strip())
    return doc[0].lemma_ if doc else word

def lemmatize_file(input_path, output_path):
    lemas = set()
    print(f"Lendo e lematizando palavras de: {input_path}")
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            word = line.strip()
            if word:
                lemma = get_lemma(word)
                lemas.add(lemma.lower())

    print(f"{len(lemas)} lemas únicos encontrados.")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(lemas)))
    print(f"Lemas salvos em: {output_path}")

if __name__ == "__main__":
    lemmatize_file(INPUT_PATH, OUTPUT_PATH)
