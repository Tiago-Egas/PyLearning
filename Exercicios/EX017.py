# Desafios métodos
from math import sqrt, pow

print('Vamos calcular o valor da Hipotenusa!')
ctOp = float(input('Informe o cateto oposto: '))
ctAd = float(input('Informe o cateto adjacente: '))

hipt = sqrt(pow(ctOp, 2) + pow(ctAd, 2))

print('Hipotenusa é igual a: {:.6f}.'.format(hipt))
