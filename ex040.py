"""Media de alunos com If"""
nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2) / 2
if media <=5:
    print(f'A sua nota foi {media} Voce está \033[1;31mREPROVADO!\033[m')
elif media < 7 > 5 :
    print(f'Você agora esta em \033[1;33mRECUPERAÇÂO!\033[m sua nota foi {media} se esforçe para passar!')
else:
    print(f'Parabéns sua media foi de {media} você esta \033[1;32mAPROVADO!\033[m')
