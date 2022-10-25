matrizA = [[],[],[]]
matrizB = [[],[],[]]
num = 0
coluna = []
quad = 0
line  = 0
col = 0
while line < 3:
    while col <3:
        num = input('digite um numero para a atriz A  ')
        if num.replace('.','', 1).replace('-','').isdigit():
            coluna.append(float(num))
            col += 1
            matrizA[line].append(coluna[:])
            coluna.clear()
        else:
            col = col
            print('digite um numero válido')
    line += 1 
    col = 0

for l in range(0,3):
    for c in range(0,3):
        quad = matrizA[l][c][0] ** 2
        matrizB[l].append([quad])

for l in range(0,3):
    for c in range(0,3):
        print(f'{matrizB[l][c]}', end ='')
    print()