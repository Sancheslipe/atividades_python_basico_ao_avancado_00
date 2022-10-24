matriz = [[],[],[],[]]
numdigitado = 0
maior = list()
maiornum = 0
for l in range(0, 4):
    for c in range(0,4):

        numdigitado = int(input('digite o valor desejado'))
        matriz[l].append(numdigitado)
        
        if numdigitado > maiornum:
            maiornum = numdigitado
            maior.clear()
            maior.append(numdigitado)
            maior.append(' na linha')
            maior.append(l+1)
            maior.append('coluna')
            maior.append(c+1)




print('\n A mnatriz é ')
print('-='*45)

for l in range(0, 4):
    for c in range(0, 4):
        print(f'{matriz[l][c]}', end=' ')
    print()

print(f' o maior valor é {maior}')