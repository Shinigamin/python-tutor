"""modulo de cores com as opções padrões do python"""
def preto(text):
    return f'\033[30m{text}\033[m'

def vermelho(text):
    return f'\033[31m{text}\033[m'

def verde(text):
    return f'\033[32m{text}\033[m'

def laranja(text):
    return f'\033[33m{text}\033[m'

def azul(text):
    return f'\033[34m{text}\033[m'

def lilas(text):
    return f'\033[35m{text}\033[m'

def ciano(text):
    return f'\033[36m{text}\033[m'

def branco(text):
    return f'\033[37m{text}\033[m'
