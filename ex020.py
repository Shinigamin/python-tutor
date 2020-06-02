"""Sorteando uma lista"""
from random import choices
al1 = str(input('\033[7;35;40mDigite o nome do Primeiro  Aluno: \033[m '))
al2 = str(input('\033[7;36;40mDigite o nome do Segundo Aluno: \033[m'))
al3 = str(input('\033[7;37;40mDigite o nome do Terceiro Aluno: \033[m'))
al4 = str(input('\033[7;31;40mDigite o nome do Quarto Aluno: \033[m'))
alunos = [al1,al2,al3,al4]
print('\033[7;34mO primeiro grupo a se apresentar e o do(da):\033[m \033[35m{}\033[m '.format(choices(alunos)))