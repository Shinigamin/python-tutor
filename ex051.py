"""Progressão Aritimitica"""
primeiro = int(input('Digite o primeiro Número: '))
razão = int(input('Digite a razão: '))
decimo = primeiro + 9 * razão
for c in range (primeiro, decimo + razão, razão):
    print(f'{c}',end= '-> ')
print('Eita')