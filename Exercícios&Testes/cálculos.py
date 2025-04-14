#Script que mostre o antecessor e sucessor de um número
n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('Antecessor: ', a , '\nSucessor: ', s)

#Script que mostre o dobro, triplo e raiz quadrada de um número
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
rq = n ** (1/2)
print('O dobro de {} é {}, o triplo de {} é {}, e a raiz quadrada de {} é {}'.format(n, d, n, t, n, rq))

#Erro cometido:
# print('O dobro de', n, 'é {}, o triplo de', n, 'é {}, e a raiz quadrada de', n, 'é {}'.format(d, t, rq))
# quando se utiliza vírgulas dentro do print, o Python separa os valores por um espaço, quando mistura isso
# com a formatação de string (como {} e format), o Python fica confuso porque está tentando formatar a string
# e ao mesmo tempo usar a vírgula para separar os parâmetros. Para isso funcionar corretamente, precisa
# colocar todos os valores de dentro do print() dentro do format()