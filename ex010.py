"""Conversor de moeda"""
print('-=-' * 20)
real = float(input('\033[33mEntre com o valor a ser convertido R$:\033[m'))
print('-=-' * 20)
dólar = real / 5.47
euro =  real / 5.96
print('Ao converter \033[35m{:.2f}\033[m os valores obtidos foram\n Você pode obter \033[31mU$:{:.2f}\033[m\n Você pode obter \033[36m£:{:.2f}\033[m'.format(real,dólar,euro))