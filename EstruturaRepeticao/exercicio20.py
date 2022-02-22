# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial
# a números inteiros positivos e menores que 16.

while True:
    fat = 1
    count = 1
    n = int(input("Fatorial de: "))
    if n < 16:
        while count <= n:
            fat *= count
            count += 1
        print(fat)
    else:
        print('Permitido apenas números menors que 16')
    sair = input('Deseja sair ? (N) Não - (S) Sim: ')
    sair = sair.upper()
    if sair == 'S':
        break
