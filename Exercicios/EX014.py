# Operações aritméticas

c = float(input('Informe a temperatura em C: '))
f = (9/5 * c) + 32
k = c + 271.15

print('{:.1f}°C corresponde a {:.1f}°F!'.format(c, f))
print('{:.1f}°C corresponde a {:.1f}K!'.format(c, k))
