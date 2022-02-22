# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez

n1 = float(input('n1 '))
n2 = float(input('n2 '))
res = (n1 + n2) / 2

if res == 10:
    print('Aprovado com distinção', res)
elif res < 7:
    print('reprovado', res)
else:
    print('aprovado', res)
