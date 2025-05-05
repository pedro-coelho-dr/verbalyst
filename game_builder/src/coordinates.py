from sklearn.decomposition import PCA
import numpy as np

def get_coordinates(target: str, hints: list[str], model) -> dict[str, tuple[float, float]]:
    words = [target] + hints
    vectors = np.array([model[word] for word in words])

    pca = PCA(n_components=2)
    coords = pca.fit_transform(vectors)

    origin = coords[0]  # target em (0, 0)
    coords -= origin

    return {
        word: (float(x), float(y))
        for word, (x, y) in zip(words, coords)
    }
