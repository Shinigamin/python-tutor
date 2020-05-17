larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('A area total e de {:.1f}'.format(area))
tinta = area / 2
print ('para pintar a parede você precisa de {:.1f} litros de tinta '.format(tinta))