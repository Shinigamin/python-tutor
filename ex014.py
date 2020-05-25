"""Conversor de temperatura"""
celsius = int(input('\033[31mDigite a temperatura em Celsius:\033[m'))
Fahrenheit = ((celsius * 9)/5) + 32
print('\033[1;30;47mA temperatura em Cºe de \033[34m{}\033[m\033[1;30;47m ao ser convertida para Fº se torna \033[33m{}\033[m'.format(celsius,Fahrenheit))