def get_distances(target: str, vocab: list[str], model) -> list[tuple[str, int]]:
    if target not in model:
        raise ValueError(f"Target '{target}' not found.")

    similarities = []
    for word in vocab:
        if word in model:
            sim = model.similarity(target, word)
            similarities.append((word, sim))

    # Ordena por similaridade decrescente
    similarities.sort(key=lambda x: x[1], reverse=True)

    # Normaliza todas as similaridades para distância 0–9999
    sims_only = [sim for _, sim in similarities]
    sim_max = max(sims_only)
    sim_min = min(sims_only)
    range_sim = sim_max - sim_min if sim_max > sim_min else 1e-6

    normalized_distance = []
    for word, sim in similarities:
        norm = 1.0 - ((sim - sim_min) / range_sim)
        distance = int(round(norm * 9999))
        normalized_distance.append((word, distance))

    return normalized_distance

