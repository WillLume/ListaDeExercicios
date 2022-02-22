# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
# Altere o programa anterior para mostrar no final a soma dos números.

lista = []
num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))
num2 -= 1
while num1 < num2:
    num1 += 1
    print(num1)
    lista.append(num1)
    soma = 0
    for n in lista:
        soma += n
print(f'A soma dos números é: {soma}')
