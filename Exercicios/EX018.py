# Desafios métodos
from math import sin, cos, tan, radians

ang = float(input('Informe um ângulo: '))

# rad = (ang * pi) / 180

sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print('')
print('Ângulo em radianos: {:.4f}.'.format(radians(ang)))
print('Seu Seno é {:.4f}.'.format(sen))
print('O Cosseno é {:.4f}.'.format(cos))
print('E a Tangente é {:.4f}.'.format(tan))
