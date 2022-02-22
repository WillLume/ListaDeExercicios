# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

lado1 = float(input('Informe o primeiro lado do triângulo: '))
lado2 = float(input('Informe o segundo lado do triângulo: '))
lado3 = float(input('Informe o terceiro lado do triângulo: '))


if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado1 + lado3) and lado2:
    if (lado1 % lado2 == 0) and (lado1 % lado3 == 0) and (lado2 % lado3 == 0):
        print('equilatero')
    elif (lado1 % lado2 != 0) and (lado1 % lado3 != 0) and (lado2 % lado3 != 0):
        print('escaleno')
    else:
        print('isósceles')
else:
    print('Não é um triângulo')
