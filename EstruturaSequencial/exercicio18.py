# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

mb = int(input('Informe o tamanho do arquivo em megas: '))
mbps = int(input('Informe quantos megas tem sua internet: '))

seg = mb / mbps
min = int(seg/60)

print('O tempo aproximádo de download é de', min, 'minutos')
