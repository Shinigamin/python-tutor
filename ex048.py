"""Soma impares Múltiplos de 3"""
num = 0
count = 0
for contagem in range(1, 501, 2):
    if contagem % 3 == 0 :
        count = count + 1
        num = num + contagem
print(f'Os multiplos de 3 ate 50 somados são um valor de {num} com um total de {count}') 