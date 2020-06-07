"""Soma de pares"""
soma = 0
num = 0
count = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c} a ser calculado: '))
    if num % 2 == 0:
        soma = num + soma
        count += 1
else:
    print(f'A soma dos valores digitados dão o total de {soma}') 