"""analisador de texto"""
cad = str(input('Digite seu nome ')).strip()
split = cad.split()
print('analisando o seu nome... ')
print('seu nome é: {}'.format(cad))
print('seu nome maiusculo é: {}'.format(cad.upper()))
print('seu nome em minusculo é {} '.format(cad.lower()))
print('Seu nome possui: {}'.format(len(cad)-cad.count(' ')))
print('Seu primeiro nome possui: {} letras.'.format(len(split[0])))



