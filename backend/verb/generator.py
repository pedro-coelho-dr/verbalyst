import json
from verb.model import load_model
from verb.config import GAMES_PATH

def normalizar_score(sim, min_sim, max_sim):
    return round((sim - min_sim) / (max_sim - min_sim) * 100)

def gerar_jogo(palavra: str, nome_arquivo: str):
    model = load_model()

    if palavra not in model:
        raise ValueError(f"A palavra '{palavra}' não está no modelo.")

    # Obtém todos os similares
    similares = model.most_similar(palavra, topn=len(model.key_to_index))

    # Extrai valores de similaridade
    valores_sim = [score for _, score in similares]
    max_sim = max(valores_sim)
    min_sim = min(valores_sim)

    # Gera ranking com score normalizado
    ranking = {
        w: normalizar_score(score, min_sim, max_sim)
        for w, score in similares
    }

    # Cria pasta se necessário
    GAMES_PATH.mkdir(parents=True, exist_ok=True)
    path_arquivo = GAMES_PATH / nome_arquivo

    # Salva arquivo JSON
    with open(path_arquivo, "w", encoding="utf-8") as f:
        json.dump({
            "palavra_do_dia": palavra,
            "ranking": ranking
        }, f, ensure_ascii=False, indent=2)

    print(f"Jogo salvo em: {path_arquivo}")
