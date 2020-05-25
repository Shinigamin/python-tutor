"""Aluguel de carro"""
#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('=-=' * 30)
km = int(input('Digite a Kilometragem rodada: '))
dias = int(input('Digite quantos dias usou o carro: '))
print('=-=' * 30)
dia = 60
pkm = 0.15
tkm = km * pkm
td = dias * dia
total = tkm+td
print('\033[1;35m Você usou o carro por {} dias\033[m, \033[1;35m ira pagar uma valor de R$:{:.2f} pelo KM rodado\033[m \033[1;35mportanto ira pagar um total de R$:{:.2f}\033[m'.format(dias,tkm,total))
