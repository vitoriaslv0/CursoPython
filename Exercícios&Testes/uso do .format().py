#utilizando .format () para facilitar a formação da mensagem no comando
n1 = int(input('Digite o número: '))
n2 = int(input('Digite o número: '))
s = n1 + n2
print('A soma entre {} e {} é: {}'.format(n1, n2, s))

n1 = int(input('Digite o número: '))
n2 = int(input('Digite o número: '))
print('A soma vale {}'.format(n1+n2))


nome = input('Digite seu nome: ')
print('Prazer em te conhecer {}!'.format(nome))

#Adicionando 20 caracteres (:20) ou (:.3f) > 3 casas flutuantes
nome = input('Digite seu nome: ')
print('Prazer em te conhecer {:20}!'.format(nome))

#Adicionando alinhamento (>direita, <esquerda, ^ centralizado)
nome = input('Digite seu nome: ')
print('Prazer em te conhecer {:>}!'.format(nome))