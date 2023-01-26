# Desafios métodos

from random import choice

al1 = str(input('Informe o nome do 1o aluno: '))
al2 = str(input('Informe o nome do 2o aluno: '))
al3 = str(input('Informe o nome do 3o aluno: '))
al4 = str(input('Informe o nome do 4o aluno: '))

aluno = choice([al1, al2, al3, al4])

print('Aluno escolhido foi: {}'.format(aluno))
