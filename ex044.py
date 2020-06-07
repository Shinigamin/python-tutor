"""Gerenciador de pagamentos"""
print('{:=^40}'.format(' Lojas Ximira '))
preço = float(input('Preço das compras R$: '))
print('''FORMAS DE PAGAMENTO
[1] À Vista dinheiro/Cheque
[2] À Vista Cartão
[3] 2x No Cartão
[4] 3x ou mais no cartão''')
opções = int(input('Qual e a opção digite a seguir:'))
if opções == 1:
    desconto = (preço * 10) / 100 
    total = preço - desconto
    print(f'Como o pagamento e a vista voce ganha 10\% e ira pagar R$:{total}')
elif opções == 2:
    desconto = (preço * 5) / 100
    total = preço - desconto
    print(f'Como o pagamento e em cartão voce ganha 5\% de desconto e pagara R$:{total}')
elif opções == 3:
    print(f'A opção selecionado foi de 2x nenhum desconto será atribuído o total e de R$:{preço}')
elif opções == 4:
    juros = (preço * 20) / 100
    total = juros + preço
    print(f'A opção selecionada foi 4 e tera um juros de 20\% o total a ser pago e de R$:{total}')
else:
    print('Opção invalidá, Tente novamente!.')