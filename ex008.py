"""Conversor de Milhas para KM"""
milhas = 1609
km = float(input(('Digite a distancia em \033[35mKilometros\033[m para ser convertida: ')))
conversor = (km * milhas) / 1000
print('A sua distancia em Km e de \033[33m{}\033[m convertidos para milha se torna \033[34m{:.2f}\033[m'.format(km,conversor))