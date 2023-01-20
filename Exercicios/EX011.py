# Operações aritméticas

alt = float(input('Altura da parede: '))
lar = float(input('Largura da parede: '))
area = alt * lar
tinta = area / 2

print('')
print('Área da parede: {}m2'.format(area))
print('Latas de tinta necessárias: {}l'.format(tinta))
