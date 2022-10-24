import random

matriz = [[],[],[],[],[]]
coluna = []


for l in range(0,5):
    for c in range(0,5):
        numRandom = (random.randint(0, 99))
        
        if numRandom in matriz:
            numRandom = (random.radint(0, 99))
            coluna.append(numRandom)
            matriz[l].append(coluna[:])
            coluna.clear()
        else:
            coluna.append(numRandom)
            matriz[l].append(coluna[:])
            coluna.clear()

for l in range(0,5):
    for c in range(0,5):
        print(f' {matriz[l][c]}',end=' , ')
    print()
