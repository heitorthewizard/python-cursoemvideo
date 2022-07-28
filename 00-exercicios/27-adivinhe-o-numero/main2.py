from random import randint
from time import sleep

random_num = randint(0, 5)
text = 'Vou pensar em um número entre 0 e 5. Tente advinhar...'

print('-' * len(text))
print(text)
print('-' * len(text))

answer = int(input('Em que número eu pensei? '))

print('Loading...')

sleep(2)

if answer == random_num:
    print('PARABÉNS! Você conseguiu me vencer')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(random_num, answer))

