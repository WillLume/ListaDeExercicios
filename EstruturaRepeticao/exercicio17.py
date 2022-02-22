# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

n = int(input("Fatorial de: "))

fat = 1
count = 1

while count <= n:
    fat *= count
    count += 1

print(fat)
