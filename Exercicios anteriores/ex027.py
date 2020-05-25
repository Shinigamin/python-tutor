nome = str(input('Digite seu nome completo: ')).strip().title()
div = nome.split()
print('Seu nome Completo é {}\n Seu primeiro nome é {}\n Seu ultimo nome é {}\n'.format(nome,div[0],div[len(div)-1]))