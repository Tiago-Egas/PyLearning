# Desafios métodos

from random import shuffle

Al1 = str(input('Primeiro nome: '))
Al2 = str(input('Segundo nome: '))
Al3 = str(input('Terceiro nome: '))
Al4 = str(input('Quarto nome: '))
alunos = [Al1, Al2, Al3, Al4]
shuffle(alunos)

print('Ordem dos alunos é: {}'.format(alunos))
