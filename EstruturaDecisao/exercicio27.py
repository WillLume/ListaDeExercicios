# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
# ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas
# e escreva o valor a ser pago pelo cliente.

kg_morango = float(input('Informe a quantidade de morangos (em kg): '))
kg_maca = float(input('Informe a quantidade de maçãs (em kg): '))

kg_frutas = kg_morango + kg_maca

if kg_morango <= 5:
    preco_morango = kg_morango * 2.50
else:
    preco_morango = kg_morango * 2.20

if kg_maca <= 5:
    preco_macas = kg_maca * 1.80
else:
    preco_macas = kg_maca * 1.50

preco_frutas = preco_morango + preco_macas

if kg_frutas >= 8 or preco_frutas >= 25:
    desconto = preco_frutas * 0.1
    valor = preco_frutas - desconto
else:
    valor = preco_frutas

print(f'O preço total é de: R${valor:.2f}')
