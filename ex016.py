"""quebrando um número"""
from math import trunc
num = float(input('\033[35mEntre com um valor: \033[m'))
print('O valor digitado foi o de \033[31m{}\033[m e sua parte inteira e \033[32m{:.0f}\033[m'.format(num,trunc(num)))
