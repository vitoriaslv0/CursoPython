#Programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = input('Digite um número de 0 a 9999: ')
print('Analisando o número',num,'...')
print('Unidade:',num[3])
print('Dezena:',num[2])
print('Centena:',num[1])
print('Milhar:',num[0])

'''ou'''

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número',num,'...')
print('Unidade:',u)
print('Dezena:',d)
print('Centena:',c)
print('Milhar:',m)