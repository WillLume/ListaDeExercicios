# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

metros_quad = int(
    input('Informe quantos metros quadrados você deseja pintar: '))
area = metros_quad * 1.1
metro = 6
litros = area / metro

lata = 18
preco_lata = 80
galao = 3.6
preco_galao = 25

somente_latas = math.ceil(litros / lata)
preco_latas = somente_latas * preco_lata

somente_galoes = math.ceil(litros / galao)
preco_galoes = somente_galoes * preco_galao

latas = math.floor(litros / lata)
total_lt = latas * preco_lata
mist_lt = litros % lata

galoes = math.ceil(mist_lt / galao)
total_gl = galoes * preco_galao
total = total_lt + total_gl


print(
    f'Se você usar somente latas usará: {somente_latas} lata(s) de tinta no total de R${preco_latas}')
print(
    f'Se você usar somente galões usará: {somente_galoes} galão(ões) de tinta no valor de total de R${preco_galoes}')
print(
    f'Se você usar misturar usará: {latas} lata(s) e {galoes} galão(ões) no valor de R${total}')
