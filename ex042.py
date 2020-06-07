"""Analisador de triangulos v2"""
r1 = float(input('Digite a primeira reta a ser utilizada: '))
r2 = float(input('Digite a segunda reta a ser utilizada: '))
r3 = float(input('Digite a terceira reta a ser utilizada: '))
if r1 < r2 + r3 and r2 < r1+r3 and r3 < r1 + r2:
    print('Um triangulo foi formado Illuminati Confirmed')
    if r1 == r2 and r2 == r3:
        print('E o mesmo e  um triangulo equilátero')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('E o mesmo e Escaleno')
    else:
        print('E o mesmo e Isósceles')
else:
    print('não foi desta vez tente novamente.')