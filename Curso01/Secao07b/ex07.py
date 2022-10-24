A = [[],[],[],[],[],[],[],[],[],[]]
coluna = 0
calculo = 0

for i in range(0,10):
    for j in range(0,10):
        if i < j: 
            
            coluna = (2*i) + (7*j) - 2
            A[i].append(coluna)
        
        elif i == j:
            
            coluna = ((3*i)**2) - 1
            A[i].append(coluna)
        
        elif i > j:
            
            coluna = ((4 * i)**3) - ((5*j)**2)
            A[i].append(coluna)




for i in range(0,10):
    for j in range(0,10):
        print(f'{A[i][j]}', end=' , ')
    print()