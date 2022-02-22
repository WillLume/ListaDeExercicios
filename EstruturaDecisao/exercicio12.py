# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
# Salário Bruto: (5 * 220): R$ 1100,00
# (-) IR (5%): R$   55,00
# (-) INSS ( 10%): R$  110,00
# FGTS (11%): R$  121,00
# Total de descontos: R$  165,00
# Salário Liquido: R$  935,00

vh = int(input('Informe seu valor hora: '))
hm = float(input('Informe suas horas trabalhadas no mês: '))
sal_bruto = vh * hm
inss = 0.1
fgts = 0.11

if sal_bruto <= 900:
    vir = 'isento'
elif sal_bruto > 900 and sal_bruto <= 1500:
    vir = sal_bruto * 0.05
elif sal_bruto > 1500 and sal_bruto <= 2500:
    vir = sal_bruto * 0.1
elif sal_bruto > 2500:
    vir = sal_bruto * 0.2

vinss = sal_bruto * inss
vfgts = sal_bruto * fgts

td = 0
if vir != 'isento':
    td = vir + vinss

sal_liq = sal_bruto - td

print(f'''
      Salário Bruto ({vh} * {hm})  : R${sal_bruto}
      (-) IR                      : R${vir}
      (-) INSS ( 10%)             : R${vinss}
      FGTS (11%)                  : R${vfgts}
      Total de descontos          : R${td}
      Salário Liquido             : R${sal_liq}
      ''')
