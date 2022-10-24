matriz = [[],[],[],[]]
coluna = 0
for l in range(0, 4):
    for c in range(0, 4):
        if l == 0:

            coluna = int(input(f'digite um numero referente á {l},{c}'))
            matriz[l].append(coluna)
        elif c == 0:
            coluna = int(input(f'digite um numero referente á {l},{c}'))
            matriz[l].append(coluna)
        else:
            coluna = '00'
            matriz[l].append(coluna)

for l in range(0,4):
    for c in range(0,4):
        if matriz[l][c] == '00':
            print('achei')  
            coluna = int(matriz[l][c]) * int(matriz[l][c])
            matriz[l][c] = coluna
        else:
            print('não achei')



for l in range(0, 4):
    for c in range(0, 4):
        print(matriz[l][c], end=' ')

    print()

