"""Tabuada"""
from time import sleep
print('***' * 20)
valor = int(input('Entre com o número a ser tabulado: ')) 
print('***' * 20)
print('processando ...')
sleep(2)
x1 = valor * 1 
x2 = valor * 2 
x3 = valor * 3 
x4 = valor * 4 
x5 = valor * 5 
x6 = valor * 6 
x7 = valor * 7 
x8 = valor * 8 
x9 = valor * 9 
x10 = valor * 10 
print('\033[33mCerto ja tenho as respostas para o valor de \033[32m{}\033[m'.format(valor))
print ('\033[31mx1\033[m =  \033[35m{}\033[m'.format(x1))
print ('\033[31mx2\033[m =  \033[35m{}\033[m'.format(x2))
print ('\033[31mx3\033[m =  \033[35m{}\033[m'.format(x3))
print ('\033[31mx4\033[m =  \033[35m{}\033[m'.format(x4))
print ('\033[31mx5\033[m =  \033[35m{}\033[m'.format(x5))
print ('\033[31mx6\033[m =  \033[35m{}\033[m'.format(x6))
print ('\033[31mx7\033[m =  \033[35m{}\033[m'.format(x7))
print ('\033[31mx8\033[m =  \033[35m{}\033[m'.format(x8))
print ('\033[31mx9\033[m =  \033[35m{}\033[m'.format(x9))
print ('\033[31mx10\033[m = \033[35m{}\033[m'.format(x10))