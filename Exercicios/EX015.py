# Operações aritméticas

km = float(input('Quantos KM foram registrados? '))
diaria = int(input('Quantos dias o carro ficou alugado? '))
ctotal = (diaria * 60) + (0.15 * km)

print('')
print('Valor a pagar com o aluguel: R$ {:.2f}.'.format(ctotal))
print('Extrato do cálculo: ')
print('Custo por KM: R$ {:>.2f}.'.format(0.15 * km))
print('Custo por diária: R$ {:>.2f}.'.format(diaria * 60))
