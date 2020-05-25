"""Pintura de parede"""
from time import sleep
print('-=-' * 20)
larg = float(input('\033[31mDigite a Largura da parede: \033[m'))
alt = float(input('\033[31mDigite a altura da parede: \033[m'))
print('-=-' * 20)
print('\033[37mEstamos calculando o valor a ser usando.\033[m')
sleep(2)
area = larg * alt
tinta = area / 2
print('\033[36mA area total da parede e de \033[32m{}\033[m \033[36msendo assim para que a mesma seja pintada de maneira eficaz e necessário usar um total de \033[35m{}\033[m \033[36mlitros para ser pintada\033[m'.format(area,tinta))