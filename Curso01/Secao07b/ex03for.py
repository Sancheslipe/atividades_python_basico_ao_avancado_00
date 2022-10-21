linha = [[],[],[],[]]

coluna = []
calculo = 0


for l in range(0,4):
    for c in range(0,4):
        if l != 0 and c == 0:
            print('linha vertical')
            
            coluna.append(int(input('Digite um numero  ')))
            linha[c].append(coluna.copy())

            coluna.clear()
        elif l == 0:
            print('linha de lado')
            coluna.append(int(input('Digite um numero  ')))
            linha[c].append(coluna.copy())
            coluna.clear()
        else:
            print((linha[(c-1)][l]))
            print(linha[c][(l-1)])
            calculo = int(linha[(c -1)][l]) * int(linha[c][(l-1)])
            print(calculo)
            coluna.append(calculo) #
            linha[c].append(coluna.copy())
            coluna.clear()
# for l in range(1,4):
#     for c in range(1,4):
#         # calculo = linha[c -1][l] * linha[c][(l-1)]
#         print(linha)
        
#         calculo = 0
#         coluna.append(calculo)
#         linha[c].append(coluna.copy())
#         coluna.clear()


print(linha)

for l in range(0,4):
    for c in range(0,4):
        print(linha[c][l], end=' ')
    print()