# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input("Qual seu nome (minimo 4 caracteres): ")
idade = int(input("Sua idade: "))
salario = float(input("Salário: "))
sexo = input("Sexo ('f' para feminino ou 'm' para masculino): ")
civil = input("Estado civil (s, c, v ou d): ")
sexo = sexo.lower
civil = civil.lower

while len(nome) <= 3:
    nome = input("Seu nome deve ter mais que 3 caracteres: ")

while (idade < 0) or (idade > 150):
    idade = int(input("Voce deve ter entre 0 e 150 anos: "))

while (salario < 0):
    salario = float(
        input("Seu salaário deve ser superior a 0: "))

while (sexo != 'f') and (sexo != 'm'):
    sexo = input("Deve ser 'f' ou 'm': ")

while (civil != 's') and (civil != 'c') and (civil != 'v') and (civil != 'd'):
    civil = input("Deve ser s, c, v ou d: ")
