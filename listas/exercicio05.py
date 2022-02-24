# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.

listanumeros = []
listapar = []
listaimpar = []
numeros = 0
print('Digite 20 números inteiros')
for num in range(20):
    listanumeros.append(int(input(f'Digite o número {num+1}: ')))
    numeros = listanumeros[num]
    if numeros % 2 == 0:
        listapar.append(numeros)
    else:
        listaimpar.append(numeros)

print(f'''
Números: {listanumeros}
Pares: {listapar}
Impares: {listaimpar}
        ''')
