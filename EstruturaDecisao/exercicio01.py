# Faça um Programa que peça dois números e imprima o maior deles.

n1 = float(input('n1 '))
n2 = float(input('n2 '))


if n1 > n2:
    print(n1)
elif n1 == n2:
    print('Os números são iguais')
else:
    print(n2)
