#Funções Random > shuffle (embaralhar elemento de uma lista)
#               > Randiant (faz o computador pensar/sortear um nmr)

#Script de sorteio
import random

aluno1 = input('Nome do aluno: ')
aluno2 = input('Nome do aluno: ')
aluno3 = input('Nome do aluno: ')
aluno4 = input('Nome do aluno: ')
lista = random.choice([aluno1, aluno2, aluno3, aluno4])
print('O sorteado foi: ', lista)

#Sortar oredem de aprensentação de alunos
import random
aluno1 = input('Nome do aluno: ')
aluno2 = input('Nome do aluno: ')
aluno3 = input('Nome do aluno: ')
aluno4 = input('Nome do aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem de aprentação será: ', lista)


