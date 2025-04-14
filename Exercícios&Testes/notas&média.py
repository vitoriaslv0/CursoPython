#Script que leia as notas de um aluno e calcule sua média
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
print('Resultado da Média:', m)
if m >= 7:
    print('Aprovado')
else:
    print('Reprovado')
#forma simplificada:
#print('Aprovado' if m >=6 else 'Reprovado')