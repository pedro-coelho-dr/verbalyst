import json
from verb.model import load_model
from verb.config import GAMES_PATH

def gerar_jogo(palavra: str, nome_arquivo: str):
    model = load_model()

    if palavra not in model:
        raise ValueError(f"A palavra '{palavra}' não está no modelo.")

    similares = model.most_similar(palavra, topn=len(model.key_to_index))
    ranking = {w: float(score) for w, score in similares}

    GAMES_PATH.mkdir(parents=True, exist_ok=True)
    path_arquivo = GAMES_PATH / nome_arquivo

    with open(path_arquivo, "w", encoding="utf-8") as f:
        json.dump({
            "palavra_do_dia": palavra,
            "ranking": ranking
        }, f, ensure_ascii=False, indent=2)

    print(f"Jogo salvo em: {path_arquivo}")
