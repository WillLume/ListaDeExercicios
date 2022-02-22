# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina)
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que:
# o preço do litro da gasolina é R$ 2,50
# o preço do litro do álcool é R$ 1,90.

# gasolina = 2.50
# porcetagem_desconto_gasolina_ate_20_litros = 3 / 100
# desconto_gasolina_ate_20_litros = gasolina * porcetagem_desconto_gasolina_ate_20_litros
# preco_gasolina_ate_20_litros = gasolina - desconto_gasolina_ate_20_litros

combustivel = input(
    'Informe qual o tipo de combustível, (A-álcool, G-gasolina): ')
litros = float(input('Informe quantos litros foram vendidos: '))

if combustivel == 'G':
    if litros <= 20:
        preco = litros * 2.43
    else:
        preco = litros * 2.38
if combustivel == 'A':
    if litros <= 20:
        preco = litros * 1.82
    else:
        preco = litros * 1.79

print(f'O valor a ser pago pelo cliente é de: R${preco:.2f}')
