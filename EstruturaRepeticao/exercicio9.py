# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

cont = 0
while cont < 50:
    cont += 1
    if cont % 2 != 0:
        print(cont)
