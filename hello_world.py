from words_data import sanitized_words
from random import choice

def inicializa(listaPal):
    return {'n' : len(listaPal[0]),
    'sorteada' : choice(listaPal),
    'especuladas' : [],
    'tentativas' : len(listaPal[0]) +1
    }


palavra = inicializa(sanitized_words)
print(palavra)