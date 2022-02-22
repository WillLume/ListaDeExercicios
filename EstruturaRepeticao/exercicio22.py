#  Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

num = int(input("Digite um número: "))
mult = 0
lista = []
for count in range(2, num):
    if (num % count == 0):
        mult += 1
        lista.append(count)

if mult == 0:
    print('É primo')
else:
    print(f'''Não é primo
Além de 1 e dele mesmo, é dividido pelos números: {lista}
    ''')
