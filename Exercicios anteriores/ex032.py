"""ano bissexto"""
from datetime import date
ano = int(input('Digite o ano a ser consultado: '))
if ano == 0:
    ano = date.today().year
if (ano%4 ==0 and ano%100!=0) or (ano%400==0):
    print('Olha quem diria {} é um ano bissexto'.format(ano))
else:
    print('Não e um ano bissexto.')
