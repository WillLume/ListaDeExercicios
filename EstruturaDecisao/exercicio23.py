# Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.

import math

num = float(input('Informe um número: '))

if num == math.floor(num):
    int_dec = 'é inteiro'

else:
    int_dec = 'é decimal'

print(int_dec)
