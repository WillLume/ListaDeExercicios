# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []
qtd = 10
for i in range(qtd):
    num = input('Digite um número: ')
    lista.append(num)
lista.reverse()
print(lista)
