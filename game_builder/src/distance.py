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

    # Em vez de normalizar entre 0–9999, usamos distância progressiva 1, 2, 3...
    normalized_distance = [(word, i + 1) for i, (word, _) in enumerate(similarities)]

    return normalized_distance
