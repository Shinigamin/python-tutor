dias = int(input('Quantos dias rodados?: '))
km =  float(input('quantos Kms rodados?:'))
carro = dias * 60
dist = km * 0.15
total = carro + dist
print ('O total a ser pago e de {:.2f}'.format(total))