"""Aumento de salario"""
salario= float(input('\033[37mDigite o seu salario: '))
aumento= int(input('Digite a porcentagem em que o mesmo será aumentando: '))
calc = (salario * aumento) / 100
total = salario + calc
print('\033[32mO seu salario atual é de R$:\033[35m{}\033[32m vai ser de \033[m\033[34mR$:{:.2f}\033[m \033[32m\033[32m apos o ajuste de \033[35m{}\033[m%'.format(salario,total,aumento))