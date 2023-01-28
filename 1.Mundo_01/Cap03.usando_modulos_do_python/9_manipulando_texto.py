from math import sqrt, pow
from random import randint
import emoji

print(emoji.emojize('Olá, Mundo!' +
                    ':hand_with_fingers_splayed:, :globe_showing_Americas:!'))
num = int(randint(1, 144))

raiz = sqrt(num)
pot = pow(raiz, 2)

print('')
print('A raiz de {} é igual a {:.2f}.'.format(num, raiz))
print('Prova dos noves: {:.2f} ao quadrado é {:.2f}.'.format(raiz, pot))
