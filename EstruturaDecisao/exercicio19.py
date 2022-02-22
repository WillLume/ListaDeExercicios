# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

import math

num = int(input('Informe um número menor que mil: '))

if num < 1000:
    num_de_cent = num / 100
    num_de_cent = math.floor(num_de_cent)
    num_de_cent = num_de_cent * 100
    aux_dez = num - num_de_cent

    num_de_dez = aux_dez / 10
    num_de_dez = math.floor(num_de_dez)
    num_de_dez = num_de_dez * 10
    aux_uni = aux_dez - num_de_dez

    num_de_uni = aux_uni
    num_de_cent = num_de_cent / 100
    num_de_dez = num_de_dez / 10

print(f'{num_de_cent:.0f} centena(s), {num_de_dez:.0f} dezena(s) e {num_de_uni} unidade(s)')
