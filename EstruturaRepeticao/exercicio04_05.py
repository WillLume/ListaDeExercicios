# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
# e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população
# o país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.


# Exercício 4:
# pop_pais_a = 80000
# cresc_pais_a = 3
# pop_pais_b = 200000
# cresc_pais_b = 1.5
while True:
    pop_pais_a = int(input('Informe a população do País A: '))
    while pop_pais_a <= 0:
        pop_pais_a = int(input('População do país deve ser maior que 0: '))
    cresc_pais_a = float(input('Informe a taxa de crescimento do País A: '))

    pop_pais_b = int(input('Informe a população do País B: '))
    while pop_pais_b <= 0:
        pop_pais_b = int(input('A população do país deve ser maior que 0: '))
    cresc_pais_b = float(input('Informe a taxa de crescimento do País B: '))

    ano = 0
    while pop_pais_a < pop_pais_b:
        ano += 1
        pop_pais_a = int((1 + (cresc_pais_a/100)) * pop_pais_a)
        pop_pais_b = int((1 + (cresc_pais_b/100)) * pop_pais_b)
    # print(f'Ano: {ano}')
    # print(f'Populaçao A: {pop_pais_a}')
    # print(f'População B: {pop_pais_b}')

    print(f'O país A irá ultrassar em população o país B em: {ano} anos')

    sair = input('Deseja sair? (s) sim ou (n) não: ')
    if sair == 's':
        break
