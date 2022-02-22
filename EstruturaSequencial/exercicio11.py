# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe outro número inteiro: '))
n3 = int(input('Informe qualquer número: '))

res1 = (n1 * 2) * (n2 / 2)
res2 = (n1 * 3) + n3
res3 = n3 ** 3

print(res1)
print(res2)
print(res3)
