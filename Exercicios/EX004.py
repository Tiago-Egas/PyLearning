# Dissecando variável informada

var1 = input('Informe alguma coisa: ')

print('')
print('Informações sobre a variável {}' .format(var1))
print('É alfanumérico?', var1.isalnum())
print('É inteiro?', var1.isnumeric())
print('É real?', var1.isdecimal())
print('É caractere?', var1.isalpha())
