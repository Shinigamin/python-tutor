""" maior e menor valores"""
print('-=-' * 25)
n1 = int(input('Digite o Primeiro valor: '))
n2 = int(input('Digite o Segundo valor: '))
n3 = int(input('Digite o Terceiro valor: '))
print ('-=-' * 25)
meno = n1
maior = n1
#menor valor
if n2<n1 and n2<n3:
    meno = n2
if n3<n2 and n3<n1:
    meno = n3
#maior valor
if n2>n1 and n2>n3:
    maior = n2
if n3>n2 and n3>n1:
    maior = n3
print('O menor número é {} e o maior número é {}'.format(meno,maior))

