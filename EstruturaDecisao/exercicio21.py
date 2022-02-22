# Faça um Programa para um caixa eletrônico.
# O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
# uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
# quatro notas de 10, uma nota de 5 e quatro notas de 1.

import math

valor = int(input('Qual valor você deseja retirar (deve ser entre 10 e 600): '))

if valor >= 10 and valor <= 600:
    notas_de_cem = valor / 100
    notas_de_cem = math.floor(notas_de_cem)
    notas_de_cem = notas_de_cem * 100
    aux_cinquenta = valor - notas_de_cem

    notas_de_cinquenta = aux_cinquenta / 50
    notas_de_cinquenta = math.floor(notas_de_cinquenta)
    notas_de_cinquenta = notas_de_cinquenta * 50
    aux_dez = aux_cinquenta - notas_de_cinquenta

    notas_de_dez = aux_dez / 10
    notas_de_dez = math.floor(notas_de_dez)
    notas_de_dez = notas_de_dez * 10
    aux_cinco = aux_dez - notas_de_dez

    notas_de_cinco = aux_dez / 5
    notas_de_cinco = math.floor(notas_de_cinco)
    notas_de_cinco = notas_de_cinco * 5
    aux_um = aux_dez - notas_de_cinco

    notas_de_um = aux_um
    notas_de_cinco = notas_de_cinco / 5
    notas_de_dez = notas_de_dez / 10
    notas_de_cinquenta = notas_de_cinquenta / 50
    notas_de_cem = notas_de_cem / 100

print(f'''{valor} reais
{notas_de_cem:.0f} nota(s) de 100
{notas_de_cinquenta:.0f} nota(s) de 50
{notas_de_dez:.0f} nota(s) de 10
{notas_de_cinco:.0f} nota(s) de 5
{notas_de_um:.0f} nota(s) de 1
        ''')
