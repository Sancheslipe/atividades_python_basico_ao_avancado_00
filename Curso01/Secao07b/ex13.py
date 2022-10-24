matriz = [[],[],[],[]]
triangular = [[],[],[],[]]
coluna = []
cont = 0
for l in range(0, 4):
    
    for c in range(0, 4):
        cont+=1
        coluna.append(1*cont)
        matriz[l].append(coluna[:])
        coluna.clear()
cont = 0

for l in range(0,4):
    
    for c in range(0,4):
        cont+=1
    
        if l == 0 and c > 0:
            coluna.append(0)
            
        elif l == 1 and c > 1:
            coluna.append(0)
            
        
        elif l ==2 and c > 2:
            coluna.append(0)

        else:
            coluna.append(1 * cont)


        triangular[l].append(coluna[:])
        coluna.clear()
            

print('\n matriz comum')
for l in range(0,4):
    for c in range(0,4):
        print(f'{matriz[l][c]}', end=',')
    print()

print('\n triangular Inferior')

for l in range(0, 4):
    for c in range(0,4):
        print(f'{triangular[l][c]}', end =' , ')
    print()
