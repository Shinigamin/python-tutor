"""Antesessor e sucessor"""
número = int(input('Digite um número: '))
ante = número - 1
suce = número + 1
print('O número digitado foi \033[31m{}\033[m e seu antecessor é \033[1;33m{}\033[m e seu sucessor é \033[1;32m{}\033[m'.format(número,ante,suce))