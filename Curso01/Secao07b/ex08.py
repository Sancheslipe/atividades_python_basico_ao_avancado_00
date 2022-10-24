matriz = [[],[],[]]
coluna = []
soma = 0

for l in range(0,3):
    for c in range(0,3):
        coluna.append(int(input('digite um numero  ')))
        matriz[l].append(coluna[:])
        if l == 0 and c ==1:
            soma += coluna[0]
        
        if l == 1 and c == 2:
            soma += coluna[0]
        coluna.clear()







print('-='*45)
print(f' a soma é {soma}')
print('-='*45)
print(f' e a matriz é \n')
for l in range(0,3):
    for c in range(0,3):
        print(f'{matriz[l][c]}', end= ' ,')
    print()

   