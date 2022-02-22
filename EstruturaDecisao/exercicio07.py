# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite um último número: '))

menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print('O menor valor é: ', menor)
print('O maior valor é: ', maior)
