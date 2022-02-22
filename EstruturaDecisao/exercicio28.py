#  Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente.
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento,
# valor do desconto e valor a pagar.

carne = input(
    'Informe a o tipo de carne, File Duplo - F, Alcatra - A, Picanha - P: ')
kg = float(input('Informe quantos kg o cliente deseja: '))
pagamento = input(
    'Informe o tipo de pagamento Dinheiro - D, Cartão Tabajara - T: ')

if carne == 'F':
    if kg <= 5:
        preco = kg * 4.90
    else:
        preco = kg * 5.80
elif carne == 'A':
    if kg <= 5:
        preco = kg * 5.90
    else:
        preco = kg * 6.80
elif carne == 'P':
    if kg <= 5:
        preco = kg * 6.90
    else:
        preco = kg * 7.80

if pagamento == 'T':
    desconto = preco * 0.05
    preco_total = preco - desconto
else:
    desconto = str('Sem desconto Aplicado')
    preco_total = preco

if carne == 'F':
    carne = 'Filé Duplo'
elif carne == 'A':
    carne = 'Alcatra'
elif carne == 'P':
    carne = 'Picanha'

if pagamento == 'T':
    pagamento = 'Cartão Tabajara'
elif pagamento == 'D':
    pagamento = 'Dinheiro'

print(f'''
    Cupom Fiscal:
Tipo da Carne - {carne}
Quantidade - {kg:.2f}kg
Preço - R${preco:.2f}
Tipo de pagamento - {pagamento}
Valor do desconto - R${desconto}
Total a pagar - R${preco_total:.2f}
        ''')
