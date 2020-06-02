"""Sorteando uma lista"""
from random import choice
al1 = str(input('\033[32mDigite o nome do Primeiro Aluno:\033[m '))
al2 = str(input('\033[32mDigite o nome do Segundo Aluno: \033[m'))
al3 = str(input('\033[32mDigite o nome do Terceiro Aluno:\033[m '))
al4 = str(input('\033[32mDigite o nome do Quarto Aluno: \033[m'))
alunos = [al1,al2,al3,al4]
print('\033[36mE você não deu muita sorte vai la apagar o quadro é a(o): \033[m \033[31m{}\033[m'.format(choice(alunos)))
