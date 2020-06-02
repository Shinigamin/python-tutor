"""Seno, Cosseno, Hipotenusa"""
import math
angulo = float(input('\033[31mDigite o angulo que você deseja: \033[m'))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('\033[4;34mO valor do seno de \033[m\033[7;34m{}\033[m \033[4;34me de\033[m \033[7;34m{:.2f}\033[m'.format(angulo,seno))

print('\033[4;35mO valor do cosseno de \033[m\033[7;35m{}\033[m\033[4;35m e de \033[m\033[7;35m{:.2f}\033[m'.format(angulo,cosseno))

print('\033[4;36mO valor da tangente de \033[m\033[7;36m{}\033[m\033[4;36m e de \033[m \033[7;36m{:.2f}\033[m'.format(angulo,tangente))