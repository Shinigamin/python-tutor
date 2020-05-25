"""Conversor de medidas"""
print('-=-' * 20)
valor = float(input('Entre com o valor a ser convertido: '))
print('-=-' * 20)
cm = valor * 100
mm = valor * 1000
print('O valor digitado de \033[36m{}\033[m ao ser convertido representa\n a \033[35m{}\033[m Centímetros\n é \033[32m{}\033[m Milimetros'.format(valor,cm,mm))
