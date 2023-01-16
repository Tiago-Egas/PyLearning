# Operações aritméticas

m = float(input('Informe medida em metros: '))
cm = m * 1000
mm = cm * 1000

print('')
print('Convertendo {:.2f} para:\n\n'
      'Centímetros: {:.2f}.\t\t'
      'Milímetros: {:.2f}'
      .format(m, cm, mm))
