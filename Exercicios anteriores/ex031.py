"""viagem"""
viagem = float(input('Qual é a distancia da sua viagem: '))
print ('Você esta prestes a começar uma viagem de {}Km '.format(viagem))
valor = viagem * 0.50
longa = viagem * 0.45
print ('O valor a ser pago e de R$:{:.2f}'.format(valor))
if viagem >= 200:
    print('Mas como é uma viagem bem longa toma aqui um descontinho, o valor ficara R$:{:.2f}'.format(longa))
print('Tenha uma Boa Viagem')