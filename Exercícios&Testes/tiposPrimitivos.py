#Tipos primitivos e informações de uma mensagem
#a = input ('Digite algo: ')
#print('O tipo primitivo é: 'type(a))
#print('Só tem espaços? ', a.isspace())
#print('É um número? ', a.isnumeric())
#print('É alfabético? ', a.isalpha())
#print('É alfanumérico?', a.isalnum())
#print('Está em maiúsculo? ', a.isupper())
#print('Está em minúsculo? ', a.islower())
#print('Está capitalizada? ', a.istitle())
# Capitalizada é quando a mensagem está em maiúsculo e minus. (Python)

n = input('Digite algo: ')
print(n.isnumeric())
#identificar um número

o = input('Digite algo: ')
print(o.isalpha())
#alphabetic : identificar uma letra

p = input('Digite algo: ')
print(p.isalnum())
#alphanumeric : identificar letra e número (A2)


  # Entendendo o comando q.isascii
q = input('Digite algo: ')
print(q.isascii())
#identiificar se há a padronização de caracetéres, sinais diversos e alguns códigos de controle
#em relação ao código ascii
# EXEMPLO:
x = ascii("My name is Ståle")
y = "My name is Ståle"
print(x)
print(y)
print(x.isascii())
print(y.isascii())


