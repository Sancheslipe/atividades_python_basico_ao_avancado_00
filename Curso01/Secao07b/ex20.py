matriz = [[],[],[]]
matrizModificada = [[],[],[]]
coluna = []
num = 0.0
somaImpar = 0
somaPar = 0
soma1e2 = 0
valor6 = []
mediaPares = 0
line = 0
col = 0
i = 0

while line <3:
    while col<6:
        num = input('digite um numero real')
        if num.replace('.','', 1).replace('-','').isdigit():
            num = float(num)
            coluna.append(num)
            matriz[line].append(coluna[:])
            coluna.clear()

            col += 1 
            
            if col %2 != 0:
                somaImpar += num

            if col == 2 or col == 4: 
                somaPar+= num                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                mediaPares = somaPar / 6

            if col == 1 or col == 2:
                soma1e2 += num
            
            if col == 3:
                valor6.append(soma1e2)
                soma1e2 = 0

        else:
            col = col
            print('digite um numero válido')
    line +=1
    col = 0

for l in range(0,3):
    for c in range(0,6):
        matrizModificada[l].append(matriz[l][c])

        if c == 5:
            matrizModificada[l].pop()
            matrizModificada[l].append([valor6[i]]) 
            i += 1



print(f'\n a soma de todos os elementos das colunas ímpares é {somaImpar}')
print(f'\n a média aritmética dos elementos da segunda coluna e da quarta coluna é {mediaPares}')

print(f'\n A matriz modificada está abaixo')
for l in range(0,3):
    for c in range(0,6):
        print(f'{matrizModificada[l][c]}', end= '')
    print()



