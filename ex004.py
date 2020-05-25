"""Dissecando uma variável"""
from time import sleep
algo = input('Digite algo a ser analisado:')
print('Processando')
sleep(1)
print('Verificamos que o objeto digitado e do tipo\033[1;35m{}\033[m'.format(type))

print('Ao digitar:\033[1;31m{}\033[m verificamos que o mesmo esta em maiusculo?\033[1;35m{}\033[m '.format(algo, algo.isupper()))

print('Ao digitar:\033[1;31m{}\033[m verificamos que o mesmo é numerico?\033[1;35m{}\033[m '.format(algo, algo.isnumeric()))

print('Ao digitar:\033[1;31m{}\033[m verificamos que o mesmo esta como titulo?\33[1;35m{}\033[m'.format(algo, algo.istitle()))

print('Ao digitar:\033[1;31m{}\033[m verificamos que o mesmo esta em minusculo?\033[1;35m{}\033[m '.format(algo, algo.islower()))

print('Ao digitar:\033[1;31m{}\033[m verificamos que o mesmo e alfanumerico?\033[1;35m{}\033[m '.format(algo, algo.isalnum()))

print('Ao digitar:\033[1;31m{}\033[m verificamos que o mesmo possui espaços?\033[1;35m{}\033[m '.format(algo, algo.isspace()))