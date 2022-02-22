# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.


import math

metros_quad = int(
    input('Informe quantos metros quadrados você deseja pintar: '))
preco_unit = 80


latas = math.ceil(metros_quad / 54)
preco_tot = latas * preco_unit
print('Você necessita de', latas,
      'lata(s) de tinta(s), no valor de R$', preco_tot)
