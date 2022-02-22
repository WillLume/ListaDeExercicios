# Faça um programa que leia 5 números e informe o maior número.

lista = []
qtd = 5
for i in range(qtd):
    n = float(input('Digite um numero: '))
    lista.append(n)

lista.sort(reverse=True)
print('0 maior valor é:', max(lista))
print('O menor valor é: ', min(lista))
print('Ordem decrescente: ', lista)
