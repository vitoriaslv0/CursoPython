#Algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produto = float(input('Qual o valor do produto? R$'))
desconto = float(input('Qual a porcentagem do desconto? '))
total = produto - (produto * desconto / 100)
print('Com o desconto de {} o produto fica R${}'.format(desconto,total))


#Algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual o salario do funcionário? R$'))
aumento = float(input('Qual a porcentagem do aumento? '))
novo_salario = salario + (salario * aumento/100)
print('Com {}% do aumento o salário passa a ser R${}'.format(aumento,novo_salario))