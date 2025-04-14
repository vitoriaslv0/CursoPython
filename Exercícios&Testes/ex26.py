#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
#No módulo todo num par dara o resultado 0, e impar 1
n = float(input('Digite um número: '))
r =  n % 2
if r == 0:
    print('O número é par')
else:
    print('O número é impar')
