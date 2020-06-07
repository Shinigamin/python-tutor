"""Classificando atletas"""
from datetime import date
nascimento = int(input('Digite o seu ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento
if idade <=9:
    print(f'O Atleta tem {idade}')
    print('Classificação:\033[35mMIRIM\033[m')
elif idade <=14 >9:
    print(f'O Atleta tem {idade}')
    print('classificação:\033[34mINFANTIL\033[m')
elif idade <=19 > 14:
    print(f'O Atleta tem {idade}')
    print('Classificação: \033[33mJUNIOR\033[m')
elif idade<=25 >19:
    print(f'O Atleta tem {idade}')
    print('Classificação: \033[32mSENIOR\033[m')
else:
    print(f'O Atleta tem {idade}')
    print('Classificação: \033[31mMASTER\033[m')