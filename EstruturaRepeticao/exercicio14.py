# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares
# e a quantidade de números impares.

cont = par = impar = 0
while cont < 10:
    num = int(input("Digite um número: "))
    cont = cont + 1
    if num % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'Números pares: {par}')
print(f'Números ímpares: {impar}')
