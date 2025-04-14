#Script que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#e calcule e mostre o comprimento da hipotenusa.
import math
n1 = float(input('Valor do cateto oposto: '))
n2 = float(input('Valor do cateto adjacente: '))
hi = math.hypot(n1, n2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

#Script que leia um ângulo e mostre o valor do seno, cosseno e tangente desse ângulo.
import math
n = float(input('Ângulo a ser calculado: '))
seno = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print ('O ângulo de {} tem o SENO de {:.2f}'.format(n, seno))
print ('O ângulo de {} tem o COSENO de {:.2f}'.format(n, cos))
print ('O ângulo de {} tem a TANGENTE de {:.2f}'.format(n, tan))