# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

lista = []
media = 0
print('Informe as 4 notas')
for nota in range(4):
    lista.append(float(input(f'Nota {nota+1}: ')))
    media += lista[nota]
media = media/4
print(f'''
Notas: {lista}
Média: {media}
        ''')
