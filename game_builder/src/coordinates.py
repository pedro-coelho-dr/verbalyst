from sklearn.decomposition import PCA
import numpy as np

def get_coordinates(target: str, hints: list[str], model, distances: dict[str, float]) -> dict[str, tuple[float, float]]:
    words = [target] + hints
    vectors = np.array([model[word] for word in words])

    # PCA projection
    pca = PCA(n_components=2)
    coords = pca.fit_transform(vectors)

    # Centralize on target (word 0)
    origin = coords[0]
    coords -= origin

    # Normalize distances
    max_real_dist = max(distances.get(word, 1.0) for word in words)

    normalized_coords = []
    for word, (x, y) in zip(words, coords):
        real_distance = distances.get(word, 1.0)
        normalized_dist = real_distance / max_real_dist

        norm = np.linalg.norm([x, y]) or 1.0  # evita divisão por zero
        direction = np.array([x, y]) / norm
        scaled = direction * normalized_dist

        normalized_coords.append((round(float(scaled[0]), 4), round(float(scaled[1]), 4)))

    return dict(zip(words, normalized_coords))
