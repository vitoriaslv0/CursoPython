#Programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
num = float(input('Digite um número: '))
print ('A porção inteira de {} é {}'.format(num, math.trunc(num)))
'''ou'''
num = float(input('Digite um número: '))
print ('A porção inteira de {} é {}'.format(num, int(num)))