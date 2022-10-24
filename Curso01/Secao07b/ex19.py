matriz = [[],[],[]]
coluna = [[],[],[],[]]
matricula = 0
mediaProvas = 0
mediaTrabalhos =0
notaFinal = 0
soma = 0
maior = 0
linha = 0
col = 0


while linha <3:
    
    while col <4:

        matricula = int(input('digite o seu numero de matricula '))
        
        mediaProvas = int(input('digite a media das suas provas '))
        mediaTrabalhos = int(input('digite a media dos trabalhos'))
        soma = mediaProvas + mediaTrabalhos
        notaFinal = soma

        if col == 0 :
            coluna.append(matricula)
            col +=1
            print(col)
        
        elif col == 1:
            coluna.append(mediaProvas)
            col +=1
            print(col)
        
        elif col == 2:
            coluna.append(mediaTrabalhos)
            col +=1
            print(col)
        elif col == 3:
            coluna.append(notaFinal)
            col +=1
            print(col)
        if notaFinal > maior:
            maior = matricula
                
        matriz[linha].append(coluna[:])
        coluna.clear()
    linha += 1
    col = 0

print(matricula)

for l in range(0,3):
    for c in range(0,4):
        print(f' {matriz[l][c]}', end= ' ')
    print()



# matriz = [[],[],[]]
# transposta = [[],[],[]]
# coluna = []
# for l in range(0,3):
#     for c in range(0,3):
#         coluna.append(int(input('digite um numero  ')))
#         matriz[l].append(coluna[:])
#         coluna.clear()

# for l in range(0,3):
#     for c in range(0, 3):
#         transposta[c].append(matriz[l][c])

# for l in range(0,3):
#     for c in range(0,3):
#         print(f' {matriz[l][c]}', end ='')
#     print()
# print('-='*45)
# print('matriz transposta')
# for l in range(0,3):
#     for c in range(0, 3):
#         print(f' {transposta[l][c]}', end = ',')
#     print()