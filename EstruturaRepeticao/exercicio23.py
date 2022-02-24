# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

num = int(input("Digite um número: "))
aux = 1
while aux < num:
    if aux % num == 0:
        aux += 1
        if aux == 0:
            print(aux)
        else:
