#Script conversor de medidas

m = int(input('Número a ser convertido: '))
mm = m * 1000
dm = m * 100
cm = m * 10
dam = m / 10
hec = m / 100
km = m / 1000
print('A conversão em milímetro resulta: {}'.format(mm))
print('A conversão em decímetro resulta: {}'.format(dm))
print('A conversão em centimetro resulta: {}'.format(cm))
print('A conversão em decâmetro resulta: {}'.format(dam))
print('A conversão em hectômetro resulta: {}'.format(hec))
print('A conversão em Quilômetro resulta: {}'.format(km))

