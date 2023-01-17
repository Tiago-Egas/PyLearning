# Operações aritméticas

m = float(input('Informe medida em metros: '))
km = m / 10
hm = m / 10
dam = m / 10
dm = m * 10
cm = m * 10
mm = cm * 10

print('')
print('Convertendo {:.2f} para:\n'
      'Kilômetros: {:.2f}\n'
      'Hectômetro: {:.2f}\n'
      'Decâmetro: {:.2f}\n'
      'Decímetro: {:.2f}.\n'
      'Centímetros: {:.2f}.\n'
      'Milímetros: {:.2f}'
      .format(m, km, hm, dam, dm, cm, mm))
