'''
#jeito certo de se inicializar e adicionar itens nas matrizes


matriz = [[],[],[],[]]
coluna = 0
for l in range(0, 4):
    for c in range(0, 4):
        coluna = int(input('digite um numero'))
        matriz[l].append(coluna)
        
        

for l in range(0, 4):
    for c in range(0, 4):
        print(matriz[l][c], end=' ')
    print()


'''