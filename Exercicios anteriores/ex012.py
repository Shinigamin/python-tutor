real = float(input('Quanto você deseja trocar: R$ '))
print()
dolar = real / 5.50
euro = real / 5.95
libra = real / 6.83
iene = real / 5.14
rupias = real / 7.23
print('Listamos alguns valores que você pode adquirir de acordo com a quantia que você deseja trocar')
print()
print('Com R$ {:.2f} você pode trocar por US$ {:.2f}'.format(real, dolar))
print('Com R$ {:.2f} você pode trocar por  €  {:.2f}'.format(real, euro))
print('com R$ {:.2f} você pode trocar por  £  {:.2f}'.format(real, libra))
print('Com R$ {:.2f} você pode trocar por  ¥  {:.2f}'.format(real,iene))
print('Com R$ {:.2f} Você pode trocar por  ₹  {:.2f}'.format(real,rupias))
print()
print(' a BR Casa de Câmbio Agradece pela Preferência, Volte Sempre!') 
print('-' * 70)