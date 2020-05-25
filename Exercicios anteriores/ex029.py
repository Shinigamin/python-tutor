"""Radar"""
vel = int(input('Qual e a Velocidade atual do carro?: '))
if vel >= 80:
    multa = (vel-80) * 7.00
    print('Piloto ta correndo e por isso vai pagar uma multilha de R$:{:.2f}'.format(multa))
print('tenha um bom dia, Dirija com segurança.')
