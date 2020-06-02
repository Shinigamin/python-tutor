"""Catetos e Hipotenosas"""
import math
cato = float(input('\033[37mInforme o valor do cateto oposto: \033[m'))
cata = float(input('\033[36mInforme o valor do cateto adjacente: \033[m'))
hip = math.hypot(cata,cato)
print('\033[34mSegue o valor da hipotenusa\033[m \033[31m{:.2f}\033[m'.format(math.hypot(hip)))
