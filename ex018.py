import math
a=float(input('Digite um ângulo que você deseja: '))
s= math.sin(math.radians(a))
c=math.cos(math.radians(a))
t=math.tan(math.radians(a))
print('O Ângulo de {} tem o Seno de {:.2f} \nO ângulo de {} tem o cosseno de {:.2f}\nO ângulo de {} tem a Tangente de {:.2f} '.format(a,s,a,c,a,t))