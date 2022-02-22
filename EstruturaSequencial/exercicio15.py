# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
# faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

sal_hora = float(input('Informe quanto você ganha por hora: '))
hora_trab = float(input('Informe quantas horas você trabalhou no mês: '))

sal_bruto = sal_hora * hora_trab

ir = sal_bruto * 0.11
inss = sal_bruto * 0.08
sind = sal_bruto * 0.05
sal_liq = sal_bruto - ir - inss - sind

print(f'''
+ Salário Bruto : R$ {sal_bruto}
- IR (11%) : R$ {ir}
- INSS (8%) : R$ {inss}
- Sindicato ( 5%) : R$ {sind}
= Salário Liquido : R$ {sal_liq}
''')

# print('Seu salário bruto é: R$', sal_bruto)
# print('Você pagou R$', inss, 'de INSS e R$', sind, 'ao sindicato')
# print('Seu salário líquido é: R$', sal_liq)
