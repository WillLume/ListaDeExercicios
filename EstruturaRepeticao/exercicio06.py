# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro.

num = 0
while num < 20:
    num = num + 1
    print(num)

num = 0
while num < 20:
    num = num + 1
    print(num, end='-')
