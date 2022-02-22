# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E

nt1 = float(input('Informe a primeira nota: '))
nt2 = float(input('Informe a segunda nota: '))

med = (nt1 + nt2) / 2

if 9 <= med <= 10:
    conceito = 'A'
    apr = 'aprovado'
elif 7.5 <= med < 9:
    conceito = 'B'
    apr = 'aprovado'
elif 6 <= med < 7.5:
    conceito = 'C'
    apr = 'aprovado'
elif 4 <= med < 6:
    conceito = 'D'
    apr = 'reprovado'
elif 0 <= med < 4:
    conceito = 'E'
    apr = 'reprovado'

print(f'''
Suas notas: {nt1} e {nt2}
Sua média: {med}
Seu conceito: {conceito}
{apr}
''')
