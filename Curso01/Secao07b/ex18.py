matriz = [[],[],[]]
coluna =[]
num = 0
soma1 = 0
soma2 = 0
soma3 = 0
somas = []

for l in range(0,3):
    for c in range(0,3):
        num = input('digite um numero ')
        coluna.append(int(num))
        matriz[l].append(coluna[:])
        coluna.clear()

        



for l in range(0,3):
    for c in range(0,3):
        print(f'{matriz[l][c]}', end= ' ')
        if c == 0:
            soma1 += matriz[l][c][0]
            
        elif c == 1:
            soma2 += matriz[l][c][0]
            
        else:
            soma3 += matriz[l][c][0]
            

    print()

somas.append(soma1)
somas.append(soma2)
somas.append(soma3)

print(f'as somas são {somas}')