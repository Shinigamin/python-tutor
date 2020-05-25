"""Escolha um numero entre 05"""
import random
from time import sleep
lista  = random.randint(0, 5)
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5 consegue advinhar... ')
print('-=-'*20)
print('processando...')
sleep(2)
escolha = int(input(('escolha um número: ')))
maquina = lista
if maquina == escolha:
    print('Acertou Miseravi 0/')
else:
    print('Errrrrrou')
print('Obrigado por tentar humano maluco, a minha escolha foi {}'.format(maquina))
