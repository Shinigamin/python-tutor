valor = float(input('Digite o valor do produto R$: '))
porc = float(input('Qual o valor da porcentagem?:'))
desc = (valor * porc)/100 
total = valor - desc
print ('O valor a ser pago com desconto e de {:.2f}'.format(total))