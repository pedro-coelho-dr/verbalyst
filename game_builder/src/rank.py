def get_word_scores(target: str, vocab: list[str], model, topn: int = 100) -> list[tuple[str, int]]:

    if target not in model:
        raise ValueError(f"Target '{target}' not found.")

    similarities = []
    for word in vocab:
        if word != target and word in model:
            sim = model.similarity(target, word)
            similarities.append((word, sim))

    # Ordenar decrescente
    similarities.sort(key=lambda x: x[1], reverse=True)
    top_similar = similarities[:topn]


    sims_only = [sim for _, sim in top_similar]
    sim_max = max(sims_only)
    sim_min = min(sims_only)

    # evitar divisão por zero
    range_sim = sim_max - sim_min if sim_max > sim_min else 1e-6

    # normalizar 0001 - 9999
    normalized_scores = []
    for word, sim in top_similar:
        norm = 1.0 - ((sim - sim_min) / range_sim)
        score = int(round(norm * 9999))
        normalized_scores.append((word, score))

    # target com score 0 no topo
    return [(target, 0)] + normalized_scores
