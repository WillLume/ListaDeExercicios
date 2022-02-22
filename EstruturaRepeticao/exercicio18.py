# Faça um programa que, dado um conjunto de N números,
# determine o menor valor, o maior valor e a soma dos valores.

lista = []
n = int(input('Informe um intervalo de números: '))
cont = 0
while cont < n:
    num = int(input("Digite um número: "))
    cont = cont + 1
    lista.append(num)
print('O maior valor é:', max(lista))
print('O menor valor é: ', min(lista))
print('Total da soma: ', sum(lista))
