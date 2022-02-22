# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme
# e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

# Faça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Fahrenheit.

n1 = float(input('n1 '))
res = 5 * ((n1-32) / 9)

print(res)

res2 = (res * 9 / 5) + 32

print(res2)
