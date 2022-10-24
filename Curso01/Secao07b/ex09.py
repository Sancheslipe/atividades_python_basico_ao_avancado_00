matriz = [[],[],[]]
coluna = []
soma = 0

for l in range(0, 3):
    for c in range(0, 3):
        coluna.append(int(input('digite um numero ')))
        matriz[l].append(coluna[:])
        if l == 1 and c == 0:
            soma += coluna[0]
        
        if l == 2 and c == 1:
            soma += coluna[0]
        coluna.clear()

print(f'\n a soma é {soma}\n')
print('-='*45,'\n')
print(' e amatriz é \n')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]}', end=' ,')
    print()

