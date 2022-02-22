# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

pergunta1 = input('Telefonou para a vítima? ')
pergunta2 = input('Esteve no local do crime? ')
pergunta3 = input('Mora perto da vítima? ')
pergunta4 = input('Devia para a vítima? ')
pergunta5 = input('Já trabalhou com a vítima? ')

part1 = 0
part2 = 0
part3 = 0
part4 = 0
part5 = 0

if pergunta1 == 'sim':
    part1 += 1

if pergunta2 == 'sim':
    part2 += 1

if pergunta3 == 'sim':
    part3 += 1

if pergunta4 == 'sim':
    part4 += 1

if pergunta5 == 'sim':
    part5 += 1

part = part1 + part2 + part3 + part4 + part5

if part <= 1:
    print('Inocente')
elif part >= 2 and part < 3:
    print('Suspeita')
elif part >= 3 and part <= 4:
    print('Cúmplice')
elif part == 5:
    print('Assassino')
