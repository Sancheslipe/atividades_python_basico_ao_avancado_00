matriz = []
resultado =[]
gabarito = []
coluna = list()
letra = ''
linha = 0
col = 0
pontos = 0


while linha < 5:
    print(f' Aluno(a) N° {linha +1}:')
    
    while col < 10:
        
        print(f'questão  {col+1}')
        
        letra = str(input('\ndigite a letra correspondente a sua resposta [A] ou [B] ou [C] ou [D]'))
        coluna.append(letra.upper())

        

        if coluna[col] == 'A':
            
            col+= 1
        
        elif coluna[col] == 'B':
              
            col+= 1
        
        elif coluna[col] == 'C':
                 
            col+= 1
        
        elif coluna[col] == 'D':
                
            col+= 1
        
        else:
            
            col = col
            coluna.pop()
            print('digite uma letra válida')
        
    matriz.append(coluna[:])
    coluna.clear()

    print(matriz)
    
    linha += 1
    col = 0


for quest in range(0,10):
    letra =str(input((f'\ndigite a resposta numero {quest+1} do gabarito  ')))
    gabarito.append(letra.upper())



for l in range(0,5):
    for c in range(0,10):

        if str(gabarito[c]) == str(matriz[l][c]):
            pontos += 1

    resultado.append(pontos)
    pontos = 0





for l in range(0,5):
    print(f'\nALUNO(A) {l+1}\n Respostas')

    for c in range(0, 10):
        
        print(f' {matriz[l][c]}', end =' , ')
    print()   
        

    print(f'-='*45)
    print(f'pontos: {resultado[l]} ')
