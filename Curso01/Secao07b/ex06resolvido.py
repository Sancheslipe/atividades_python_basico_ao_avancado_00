matriz1 = [[],[],[],[]]
matriz2 = [[],[],[],[]]
matriz3 = [[],[],[],[]]
coluna = 0

for l in range(0,4):
    for c in range(0,4):
        coluna = int(input(f'digite os numeros referente á primeira matriz   '))
        matriz1[l].append(coluna)

for l in range(0,4):
    for c in range(0,4):
        coluna = int(input('digite os numeros referente a segunda matriz   '))
        matriz2[l].append(coluna)

for l in range(0,4):
    for c in range(0,4):
        
        if matriz1[l][c] > matriz2[l][c]:
            matriz3[l].append(matriz1[l][c])
        elif matriz2[l][c] > matriz1[l][c]:
            matriz3[l].append(matriz2[l][c])
        elif matriz2[l][c] == matriz1[l][c]:
            matriz3[l].append(matriz1[l][c])


print('\-/'*45)
print(f'esta é a matriz 1')

for l in range(0, 4):
    for c in range(0, 4):
        print(f'{matriz1[l][c]}', end=' ')
    print()

print('\-/'*45)
print(f'esta é a matriz 2')

for l in range(0, 4):
    for c in range(0, 4):
        print(f'{matriz2[l][c]}', end=' ')
    print()

print('\-/'*45)
print(f'esta é a matriz 3 ( a que possui a com os maiores indices')

for l in range(0, 4):
    for c in range(0, 4):
        print(f'{matriz3[l][c]}', end=' ')
    print()