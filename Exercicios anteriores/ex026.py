"""primeira e ultima ocorrencia de uma string"""
frase = str(input('Digite a sua frase: ')).strip().lower()
print('sua frase possui {} vezes a letra (a) repitadas '.format(frase.count('a')))

print('A primeira vez que a letra (a) foi encontrado foi na {} posição '.format(frase.find('a')+1))

print('A ultima ocorrencia da letra (a) foi encontrada na {} posição '.format(frase.rfind('a')+1))


