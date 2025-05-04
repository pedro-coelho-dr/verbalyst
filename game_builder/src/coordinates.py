from sklearn.manifold import MDS
from sklearn.metrics.pairwise import cosine_distances
import numpy as np

def get_relative_coordinates_mds(target: str, hints: list[str], model) -> dict[str, tuple[float, float]]:
    words = [target] + hints
    vectors = np.array([model[word] for word in words])
    
    dist_matrix = cosine_distances(vectors)
    mds = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
    coords = mds.fit_transform(dist_matrix)
    
    origin = coords[0]
    coords -= origin

    return {
        word: (float(x), float(y))
        for word, (x, y) in zip(words, coords)
    }
