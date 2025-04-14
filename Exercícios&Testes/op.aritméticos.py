#Operadores e sua ordem de precedência
#1- ()
#2- **
#3- *, /, //, %
#4- + e -

#Raiz Quadrada: **(1/2)
#Raiz Cúbica: **(1/2)

# = Igual
#!= Diferente
# < Menor que
# > Maior que
# <= Menor ou igual
# >= Maior ou igual

n1 = int(input('Digite o número: '))
n2 = int(input('Digite o número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {}, a divisão é {}'.format(s, m, d), end=' ')
print('A divisão inteira é {} e a potência é {}'.format(di, e))


