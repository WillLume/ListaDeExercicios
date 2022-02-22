# Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).

num = int(input('Informe um número inteiro: '))

if num % 2 == 0:
    par_impar = 'é par'
else:
    par_impar = 'é impar'

print(par_impar)
