# Operações aritméticas

n1 = int(input('Informe um número: '))

print('')
print('Valor informado: {}.\n'
      'Dobro: {}.\n'
      'Triplo: {}.\n'
      'Raiz Quadrada: {:.2f}.'
      .format(n1, (n1 * 2), (n1 * 3), (n1 ** (1/2))))
