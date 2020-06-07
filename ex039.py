from datetime import date
nascimento = int(input('digite o seu ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
if idade == 18:
    print(f'Voce possui {idade} e deve se alistar este ano.')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você ainda não possui idade para se alistar')  
    ano = atual + saldo
    print(f'Seu alistamento devera ser em {ano}')
elif idade > 18:
    saldo = idade - 18
    print(f'Voce possui {idade} anos e deve se alistar IMEDIATAMENTE!!!')
    ano = atual - saldo
    print(f'Voce deveria ter se alistado em {ano}')