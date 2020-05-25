"""Aumento de salario"""
salario = float(input('Digite o Valor do seu salario: '))
if salario >= 1250.00:
    aumento = salario + (salario * 10 / 100)
    print('O seu novo salario sera de {:.2f}'.format(aumento))
else:
    salario <= 1250.00
    aumento = salario + (salario * 15 / 100)
    print('O seu novo salario será de R$ {:.2f}'.format(aumento))
print('Obrigado tenha um bom dia.')