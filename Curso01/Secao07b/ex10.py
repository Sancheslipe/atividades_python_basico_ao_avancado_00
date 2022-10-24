matriz = [[],[],[]]
coluna = []
soma = 0

for l in range(0,3):
    for c in range(0,3):
        coluna.append(int(input('digite um numero')))
        matriz[l].append(coluna[:])
        
        if l == 0 and c == 0:
            soma += coluna[0]
        elif l == 1 and c == 1:
            soma += coluna[0]
        elif l ==2 and c == 2:
            soma += coluna[0]
        coluna.clear()

print(f'\n A soma é {soma}')
print('-='*45)
print('a matriz é :')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]}', end=',')
    print()
