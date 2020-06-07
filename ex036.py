"""Aprovando emprestimo"""
casa = int(input('Digite o valor da casa que deseja comprar: '))
salario=int(input('Digite o valor do seu salario: '))
anos = int(input('Digite em quantos anos deseja pagar o imovel:'))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
if prestação <= minimo:
    print('\033[31mParabens!!!\033[m \033[32mseu credito foi aprovado, ja e possível comprar a casa.\033[m')
else:
    print('Desculpe, mas voce não possui fundos o suficiente para ter o emprestimo aprovado, tente novamente em alguns meses.')