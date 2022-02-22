# Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58.

# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7


h = float(input('Informe sua altura: '))

resh = (72.7*h) - 58

resm = (62.1*h) - 44.7

print('O peso ideal para homens é:', resh)
print('O peso ideal para mulheres é:', resm)


# s = ('Informe sua sexualidade: ')
# s = s.upper()
# if s == 'M':
#     hm = float(input('Informe sua altura: '))
#     resm = (72.7*hm) - 58
#     print('Seu peso idela é: ', resm)
# elif s == 'F':
#     hf = float(input('Informe sua altura: '))
#     resf = (62.1*hf) - 44.7
#     print('Seu peso idela é: ', resf)
# else:
#     ('Informe um valor válido')


# h = float(input('Informe sua altura: '))s
# s = input('Informe sua sexualidade: ')
# resM = (72.7*h) - 58
# resF = (62.1*h) - 44.7
# s = s.upper()
# if s == 'M':
#     print('Seu peso idela é: ', resM)
# elif s == 'F':
#     print('Seu peso idela é: ', resF)
# else:
#     ('Informe um valor válido')

# s = input('Informe seu sexo: ')
# h = float(input('Informe sua altura em metros: '))

# if s == 'm':
#     res = round((72.7 * h) - 58, 2)
# else:
#     res = round((62.1 * h) - 44.7, 2)

# print('Seu peso ideal é', res)
