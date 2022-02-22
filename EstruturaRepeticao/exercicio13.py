# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

potencia = 1
# count = num2
for count in range(num2):
    potencia *= num1
    count += 1
print(potencia)
