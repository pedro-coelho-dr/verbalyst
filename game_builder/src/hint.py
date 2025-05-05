import random

def get_hints(target: str, vocab: list[str], model, distances: list[tuple[str, int]], num_hints: int) -> list[str]:
    if len(distances) < num_hints:
        raise ValueError("Not enough distance entries to select hints.")

    # Ordenar por distância (menor = mais próxima do target)
    distances.sort(key=lambda x: x[1])

    # Pegar top N * 10 mais próximas
    top_k = num_hints * 10
    top_dists = distances[:top_k]

    # Dividir em N faixas e sortear 1 de cada
    bin_size = len(top_dists) // num_hints
    hints = []
    for i in range(num_hints):
        bin_slice = top_dists[i * bin_size : (i + 1) * bin_size]
        if bin_slice:
            word = random.choice(bin_slice)[0]
            hints.append(word)

    return hints