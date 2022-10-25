matriz1=[[],[],[]]
matriz2=[[],[],[]]
matriz3 = [[],[],[]]
line = 0
col = 0
coluna = []
multi = 0

while line <3:
    while col <3:
        num = input(f'digite um numero referente á posição {line},{col} na primeira matriz  ')
        if num.replace('.','', 1).replace('-','').isdigit():
            coluna.append(float(num))
            matriz1[line].append(coluna[:])
            coluna.clear()
            col+=1
        
        else:
            col = col
            print('digite um numero válido')
    line+=1
    col = 0

line = 0
col = 0

while line <3:
    while col <3:
        num = input(f'digite um numero referente á posição {line},{col} na Segunda matriz  ')
        if num.replace('.','', 1).replace('-','').isdigit():
            coluna.append(float(num))
            matriz2[line].append(coluna[:])
            coluna.clear()
            col+=1
        
        else:
            col = col
            print('digite um numero válido')
    line+=1
    col = 0

for l in range(0,3):
    for c in range(0,3):
        multi = matriz1[l][c][0] * matriz2[l][c][0]
        matriz3[l].append(multi)

print(f' a multiplicação da matriz 1 pela matriz 2 é ')

for l in range(0,3):
    for c in range(0,3):
        print(f'{matriz3[l][c]}', end = ' , ')
    print()