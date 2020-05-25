"""Calculando desconto"""
valor = float(input('\033[31mDigite o valor a receber o desconto: \033[m'))
desconto = float(input('\033[35mDigite o valor do desconto: \033[m'))
calc = (valor * desconto) / 100
total = valor - calc
print('O valor original do produto e de R$:\033[31m{}\033[m e com o desconto de \033[33m{}\033[m% tem seu valor alterado para R$:\033[1;33m{}\033[m'.format(valor,desconto,total))