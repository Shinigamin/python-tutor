"""JOKENPO"""
escolha1 = (int(input('''Suas opções são
[1] Pedra
[2] Papel
[3] Tesoura
Qual a sua jogada?: ''')))
escolha2 = (int(input('''Suas opções são
[1] Pedra
[2] Papel
[3] Tesoura
Qual a sua jogada?: ''')))

if escolha1 == 1 and escolha2 == 2:
    print('Papel ganha de pedra jogador 2 ganhou!')
elif escolha1 == 2 and escolha2 ==1:
    print('Papel ganha de pedra jogador 1 Ganhou')
elif escolha1 == 2 and escolha2 == 3:
    print('Tesoura ganha de papel jogador 1 Ganhou')
elif escolha1 == 3 and escolha2 == 2:
    print('Tesoura ganha de papel jogador 2 Ganhou')
elif escolha1 == 1 and escolha2 == 3:
    print('Pedra Ganha de tesoura Jogador 1 Ganhou')
elif escolha1 == 3 and escolha2 == 1:
    print('Pedra Ganha de tesoura Jogador 2 Ganhou')
elif escolha1 == escolha2:
    print('Ambos escolheram a mesma opção tente novamente')
else:
    print('Tente Novamente opção invalida.')