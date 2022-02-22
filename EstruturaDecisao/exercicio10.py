# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem:
# "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

valor1 = input('Informe seu turno: ')
valor1 = valor1.upper()
if valor1 == 'M':
    print('Bom dia')
elif valor1 == 'V':
    print('Boa tarde')
elif valor1 == 'N':
    print('Boa noite')
else:
    print('Informação inválida')
