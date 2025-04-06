import random
from verb.model import load_model

def escolher_palavra_do_dia():
    model = load_model()
    palavras = list(model.key_to_index.keys())
    return random.choice(palavras)