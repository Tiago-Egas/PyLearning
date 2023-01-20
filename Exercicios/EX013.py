# Operações aritméticas

sal = float(input('Informe o salário: '))
aumt = sal * 1.15

print('')
print('O salário deR$ {:.2f}, com aumento de 15%: R$ {:.2f}'.format(sal, aumt))
print('Valor do aumento: R$ {:.2f}!'.format(aumt - sal))
