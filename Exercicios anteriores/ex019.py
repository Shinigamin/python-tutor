import random
primeiro=input('Digite o primeiro aluno: ')
segundo=input('Digite o segundo aluno: ')
terceiro=input('Digite o terceiro aluno: ')
quarto=input("Digite o quarto aluno: ")
lista = [primeiro,segundo,terceiro,quarto]
print ('O aluno escolhido foi {}'.format(random.choice(lista)))