"""Analisador de triangulos v1"""
r1 = float(input('Digite a primeira reta a ser utilizida: '))
r2 = float(input('Digite a segunda reta a ser utilizida: '))
r3 = float(input('Digite a terceira reta a ser utilizida: '))
if r1 < r2 + r3 and r2 < r1+r3 and r3 > r1 + r2:
    print('Um tringulo foi formado Illuminati Confirmed')
else:
    print('não foi desta vez tente novamente.')