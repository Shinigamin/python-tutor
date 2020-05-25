"""Media de alunos"""
print('***' * 10)
nota1 = float(input('\033[4;31;47mDigite a primeira nota do Aluno:\033[m'))
nota2 = float(input('\033[4;32;33mDigite a segunda nota do Aluno:\033[m'))
print('***' * 10)
media = (nota1 + nota2) / 2
print('A media do aluno foi de \033[1;31m{:.1f}\033[m '.format(media))