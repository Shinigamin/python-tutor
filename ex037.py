"""Conversor Binario, Octal, Hexa"""
import cores

num = int(input('Digite um número inteiro: '))
print('[1] Para converter para Binario')
print('[2] Para converter para Octal')
print('[3] Para converter para Hexadecimal')
opção = int(input('Sua opção: '))

BINARIO = 1
OCTAL = 2
HEXA = 3

print (f'a sua opção foi {opção}')

if opção == 1:
    print(f'{num} convertido em BINARIO e de {bin(num)[2:]}')


elif opção == 2:
    print(f'{num} convertido em OCTAL e de {oct(num)[2:]}')


elif opção == 3:
    print(f'{num} convertido em HEXADECIMAL e de {hex(num)[2:]}')


else:
    print('Escolha uma das opções informadas anteriormente.')
