"""Comparando numeros"""
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
if num2 < num1:
    print(f'o primeiro valor de {num1} e maior do que o segundo ')
elif num1 < num2:
    print(f'O Segundo valor de {num2} e maior do que o primeiro')
else:
    print('Os 2 Números são iguais.')
