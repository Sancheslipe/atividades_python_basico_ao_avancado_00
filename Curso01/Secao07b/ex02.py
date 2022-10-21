matriz = [[], [], [], [], []]
coluna = []

for l in range(0,5):
    for c in range(0,5):
        
        if (l == 0) and (c == 0):
            coluna.append(1)
            matriz[c].append(coluna.copy())
            coluna.clear()
        elif (l == 1) and (c == 1):
            coluna.append(1)
            matriz[c].append(coluna.copy())
            coluna.clear()
        elif (l == 2) and (c == 2):
            coluna.append(1)
            matriz[c].append(coluna.copy())
            coluna.clear()
        elif (l == 3) and (c == 3):
            coluna.append(1)
            matriz[c].append(coluna.copy())
            coluna.clear()
        elif (l == 4) and (c == 4):
            coluna.append(1)
            matriz[c].append(coluna.copy())
            coluna.clear()
        else:
            coluna.append(0)
            matriz[c].append(coluna.copy())
            coluna.clear()
print('-='*30, '\n')
for l in range(0,5):
    for c in range(0,5):
        print(f'{matriz[l][c]}' ,end='')
    print()