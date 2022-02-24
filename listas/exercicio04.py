# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lista = []
consoantes = 0
print('Digite 10 caracters')
for letra in range(10):
    lista.append(input(f'Caracter {letra+1}: '))
    char = lista[letra]
    if char in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
        consoantes += 1
print(f'Foram digitadas {consoantes} consoantes')
