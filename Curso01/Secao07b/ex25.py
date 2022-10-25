
matriz = [[0,0,0],[0,0,0],[0,0,0]]
num = 0
executar = True
linha = 0
coluna = 0
jogadas = 0
Ia = 0
no_play = ''

while executar == True:
    for l in range(0,3):
        for c in range(0,3):
            print(f'[{matriz[l][c]}]', end ='')
        print()


    while jogadas < 8:
            print(f'voce tem {8 - jogadas} jogadas')
            
            linha = int(input('linha'))
            
            if linha <= 2:
                coluna = int(input('coluna'))
                if coluna <= 2:

                    if matriz[linha][coluna] == 0 : 
                        jogadas +=1
                        
                        for l in range(0,3):
                            for c in range(0,3):
                                
                                matriz[linha][coluna] = 1
                                print(f'[{matriz[l][c]}]',end='')
                            print()

                    no_play = str(linha)+str(coluna)
                    ia 
                    ia = [  ['00','01','02'],
                            ['10','11','12'],
                            ['20','21','22']
                        ]   
                    print(ia[0][1][0])
                    print(ia[0][1][1])                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                elif matriz[linha][coluna]  != 0:

                    jogadas = jogadas
                    print('escolha outra posição para jogar')
                    
                else:
                    jogadas = jogadas
                    print('digite uma coluna entre 0 e 2 ')
            
            else:
                jogadas = jogadas
                print('digite uma linha entre 0 e 2')

    executar = False

print('Partida encerrada !')   