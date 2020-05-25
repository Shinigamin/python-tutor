"""Formatação inicial """
nome = str(input('Digite seu nome Completo: ')).strip()
print('Analisando seu nome... ')
print('Seu nome em maiusculas é: {}'.format(nome.upper()))
print('Seu nome em minusculas é: {}'.format(nome.lower()))
print('Seu nome em tem um total de: {}'.format((len(nome)-nome.count(' '))))
print('Seu nome tem {}'.format(nome.find(' ')))