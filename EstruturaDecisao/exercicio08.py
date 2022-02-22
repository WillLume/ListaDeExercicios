# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

n1 = float(input('Informe o valor do produto: '))
n2 = float(input('Informe o valor do produto: '))
n3 = float(input('Informe o valor do produto: '))

menor = n1

if menor > n1:
    menor = n2
if menor > n3:
    menor = n3

print(
    'Você deve comprar o produto que possui o preço de: R${:.2f}'.format(menor))
