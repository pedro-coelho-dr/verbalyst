from sklearn.decomposition import PCA
import numpy as np

def get_coordinates(target: str, hints: list[str], model, distances: dict[str, float]) -> dict[str, tuple[float, float]]:
    words = [target] + hints
    vectors = np.array([model[word] for word in words])

    # PCA projection
    coords = PCA(n_components=2).fit_transform(vectors)

    # Centralize on target (word 0)
    coords -= coords[0]

    max_real_dist = max(distances.get(word, 1.0) for word in words)
    min_radius = 0.2
    exponent = 0.9

    adjusted_coords = []
    for word, (x, y) in zip(words, coords):
        real_distance = distances.get(word, 1.0)
        scaled_dist = min_radius + (real_distance / max_real_dist) ** exponent

        direction = np.array([x, y]) / (np.linalg.norm([x, y]) or 1.0)
        final = direction * scaled_dist
        adjusted_coords.append((float(final[0]), float(final[1])))

    # Normalize final coordinates to fit inside a unit circle
    max_radius = max(np.linalg.norm(c) for c in adjusted_coords) or 1.0
    final_coords = [(round(x / max_radius, 4), round(y / max_radius, 4)) for x, y in adjusted_coords]

    return dict(zip(words, final_coords))
