#Conversão uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Digite a quantidade de graus: '))
f = celsius * 1.8 + 32
print('A temperatura de {0}°C corresponde a {1}°F'.format(celsius, f))



#Script que pergunte a quantidade de Km percorridos e qnt dias por um carro alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = float(input('O carro foi utilizado por quantos dias? '))
km = float(input('Quantidade de Km rodados: '))
total = (dias * 60) + (km * 0.15)
print('O total do aluguel do carro é ', total)