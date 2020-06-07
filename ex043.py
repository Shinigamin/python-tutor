"""Calculo de IMC"""
peso = float(input('Qual o seu peso em (KG)?: '))
altura = float(input('Qual a sua altura em (M)?:'))
imc = peso / (altura ** 2)
print(f'O Seu IMC e de {imc:.1f}')
if imc <=18.5:
    print('Você esta \033[1;36mABAIXO DO PESO.\033[m')
elif imc <= 25:
    print('\033[1;33mPeso Ideal Parabéns.\033[m')
elif imc <=30:
    print ('\033[34mSobrepeso Cuidado.')
elif imc <=40:
    print('\033[31mObesidade\033[m')
else:
    print('\033[1;31mOBESIDADE MORBIDA!!! Cuidado!!!')