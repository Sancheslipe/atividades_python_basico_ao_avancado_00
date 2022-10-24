matriz = [[],[],[]]
transposta = [[],[],[]]
coluna = []
for l in range(0,3):
    for c in range(0,3):
        coluna.append(int(input('digite um numero  ')))
        matriz[l].append(coluna[:])
        coluna.clear()

for l in range(0,3):
    for c in range(0, 3):
        transposta[c].append(matriz[l][c])

for l in range(0,3):
    for c in range(0,3):
        print(f' {matriz[l][c]}', end ='')
    print()
print('-='*45)
print('matriz transposta')
for l in range(0,3):
    for c in range(0, 3):
        print(f' {transposta[l][c]}', end = ',')
    print()