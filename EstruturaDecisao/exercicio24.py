# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

import math

num1 = float(input('Informe um número: '))
num2 = float(input('Informe outro número: '))
oper = input('Informe uma operação matemática (+ - * /): ')

if oper == '+':
    res = num1 + num2
elif oper == '-':
    res = num1 - num2
elif oper == '*':
    res = num1 * num2
elif oper == '/':
    res = num1 / num2

if res % 2 == 0:
    par_impar = 'é par'
else:
    par_impar = 'é impar'

if res >= 0:
    pos_neg = 'é positivo'
else:
    pos_neg = 'é negativo'

if res == math.floor(res):
    int_dec = 'é inteiro'

else:
    int_dec = 'é decimal'

print(f'''
{res}
{par_impar}
{pos_neg}
{int_dec}
        ''')
