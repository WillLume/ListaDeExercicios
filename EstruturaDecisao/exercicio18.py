# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input('Informe qualquer dia: '))
mes = int(input('Informe qualquer mês: '))
ano = int(input('Informe qualquer ano: '))

data = False

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia <= 31:
        data = True
if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 30:
        data = True
if mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        if dia <= 29:
            data = True
    elif dia <= 28:
        data = True

print(f'{dia:0>2}/{mes:0>2}/{ano}')
if (data):
    print('data válida')
else:
    print('data inválida')
