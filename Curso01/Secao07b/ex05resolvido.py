matriz = [[],[],[],[],[]]
coluna = 0
x = 0
achei = False
localizacao = list()
for l in range(0, 5):
    for c in range(0, 5):
        coluna = int(input(' digite o numero desejado'))
        matriz[l].append(coluna)

x = int(input(' digite o numero X'))

for l in range(0,5):
    for c in range(0,5):

        if x == matriz[l][c]:
            achei = True
            localizacao.append('está na linha')
            localizacao.append(l+1)
            localizacao.append('esta na coluna')
            localizacao.append(c+1)
            






if achei == True:
    print(f' o numero {x} {localizacao}')
elif achei == False:
    print('não encontrado ')

print(' a matriz é \n')
print('\='*45)
for l in range(0,5):
    for c in range(0,5):
        print(f' {matriz[l][c]}', end=' ,')
    print()

