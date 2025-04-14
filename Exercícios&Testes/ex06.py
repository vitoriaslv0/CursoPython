#Script que leia a altura e largura de uma parede em metros, calcule sua área
#e a quantidade de tinta necassária para limpa-la (1l = 2m²)
larg = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))
area = larg * alt
print('A dimensão da parede é de {}x{}, e sua área possui {}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintá-la é necessário {:.2f}l de tinta.'.format(tinta))

