#Utilizando Módulos
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print ('A raiz de {} é igual a {:.2f}'.format(num, raiz))
#Sqrt > raiz quadrada
#Arredondar para cima > .format(num, math.ceil())
#Arredondar para baixo > .format(num, math.floor())
#Eliminar da vírgula p/ frente > .format(num, math.trunc())
#Potência de um número > .format(num, math.pow())
#Equação fatorial > factorial

from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print ('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))
#com o "from math import sqrt, floor, encurta e facilita o script.
#o floor utilizado no inicio do comando nao necessita do math. depois

#Aleatorizar números
import random
num = random.choice([1,10])
print(num)




