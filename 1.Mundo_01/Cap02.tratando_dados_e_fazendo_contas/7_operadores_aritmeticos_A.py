# Operadores aritmeticos
# Ordem de precedência
# 1. parenteses ()
# 2. exponenciação (**)
# 3. multiplicação (*), divisão (/),
#    divisão inteira (//), resto da divisão (%)
# 4. soma (+), subtração (-)

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('Soma {} \nProduto {} \nDivisao {} \n'
      .format(s, m, d), end="")
print('Div inteira {} \nPotência {}'
      .format(di, e))
