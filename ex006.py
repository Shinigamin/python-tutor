"""Dobro, Triplo, Raiz quadrada"""
print('-=-' * 25)
valor = int(input('\033[7;30;43mDigite um valor a ser calculado:\033[m'))
print('-=-' * 25)
dobro = (valor * 2)
triplo = (valor * 3)
rq = valor ** 0.5
print('Aqui estão os valores calculados de \033[34m{}\033[m, O dobro de \033[36m{}\033[m , Já o triplo é de \033[31m{}\033[m, e sua raiz quadrada e de \033[32m{:.1f}\033[m'.format(valor,dobro,triplo,rq))
