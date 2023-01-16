# Operações aritméticas

real = float(input('Dinheiro na carteira: '))
dolar = real * 5.10             # cotação em 15/01/23
euro = real * 5.53              # cotação em 15/01/23

print('')
print('BRL/USD: {:.2f}'.format(dolar))
print('BRL/EUR: {:.2f}'.format(euro))
