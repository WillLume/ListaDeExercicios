# Faça um Programa que leia três números e mostre-os em ordem decrescente

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite um último número: '))

if n3 > n2:
    aux = n3
    n3 = n2
    n2 = aux

if n2 > n1:
    aux = n2
    n2 = n1
    n1 = aux

if n3 > n2:
    aux = n3
    n3 = n2
    n2 = aux

print(n1, n2, n3)
