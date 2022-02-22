# Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite um último número: '))

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print('O maior valor é:', maior)


# lista = []
# qtd = 3
# for i in range(qtd):
#     n = float(input('Digite um numero: '))
#     lista.append(n)

# lista.sort(reverse=True)
# print('0 maior valor é:', max(lista))
# print('O menor valor é: ', min(lista))
# print('Ordem decrescente: ', lista)
