import random
from time import sleep
print('-.'*25)
print('Vou pensar em número de 0 a 10. Tente adivinhar...')
print('-.'*25)
n= int(input('Em que número eu pensei? '))
m = random.randint(0,100)
if n == m:
    print('PROCESSANDO...')
    sleep(2)
    print('Você me venceu. Parabéns!')
else:
    print('PROCESSANDO...')
    sleep(2)
    print('Você perdeu!')
