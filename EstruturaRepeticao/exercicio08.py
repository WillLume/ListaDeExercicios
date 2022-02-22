# Faça um programa que leia 5 números e informe a soma e a média dos números.
lista = []
qtd = 5
for i in range(qtd):
    num = float(input('Informe um número: '))
    lista.append(num)
    soma = 0
    for n in lista:
        soma += n
        med = soma / 5
print(f'''
        A soma dos números é: {soma}
        A média dos números é: {med}
    ''')
