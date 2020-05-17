'''co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

import math
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('comprimento do cateto adjaceste '))
hi = math.hypot(co,ca)
print ('A hipotenusa vai medir {:.2f}'.format(math.hypot(hi)))