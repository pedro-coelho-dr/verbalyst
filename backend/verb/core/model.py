from gensim.models import KeyedVectors
from verb.core.config import MODEL_PATH

_model = None

def load_model():
    global _model
    if _model is None:
        _model = KeyedVectors.load(str(MODEL_PATH), mmap='r')
    return _model