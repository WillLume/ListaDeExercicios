# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000

lista = []
n = float(input('Informe um intervalo de números: '))
cont = 0
while cont < n:
    num = int(input("Digite um número: "))
    if num > 0 and num < 1000:
        cont = cont + 1
        lista.append(num)
    else:
        print('Apenas valores entre 0 e 1000')
print('O maior valor é:', max(lista))
print('O menor valor é: ', min(lista))
print('Total da soma: ', sum(lista))
