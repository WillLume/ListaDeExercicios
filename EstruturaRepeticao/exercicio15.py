# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.

n = int(input('Informe qualquer valor: '))
ultimo = 1
penultimo = 1
fib = 0
print('0')
print(ultimo)
print(penultimo)
while fib < n:
    fib = ultimo + penultimo
    penultimo = ultimo
    ultimo = fib
    print(fib)
