# matrix = [[],[],[],[]] 
lista = [] 
coluna = []
num = 0 
cont1 = 0
cont2 = 0
contador1 = 0
contador2 = 0
calculo = 0

while cont1 <= 3:
    while cont2 <=3:
        
        if (cont1 == 0):

            num = int(input(f'digite um numero referente á {cont1 },{cont2}  '))
            
            # coluna.append(f'X {cont1}')
            # coluna.append(f'Y {cont2}')            
            coluna.append(num) 
            lista.append(coluna.copy())
            # lista.insert(cont2, coluna.copy()) #
            coluna.clear()
            
            print(lista)

        else:
            if (cont2 == 0):
                num = int(input(f'digite um numero referente á {cont1 },{cont2}  '))
                
                # coluna.append(f'X {cont1}')
                # coluna.append(f'Y {cont2}')
                coluna.append(num)
                # lista[cont2].append(coluna.copy())
                # coluna.append(num)
                lista[cont2].insert(cont1,coluna.copy()) #NÃO DEU BOA CONTINUA SENDO ADICIONADO COMO LISTA DENTRO DE LISTA
                coluna.clear()

                
                print(lista[cont2])

                # print(f'primeira coluna horizontal cont2 {coluna}')
        #end if      
        
        cont2 += 1
        
    # end while
    cont1 +=1
    cont2 = 0
# end while
# print(lista) #IT'S RUNNING BOY HEHEHE

contador1 = 0
contador2 = 0

while contador1 <=3:
    while contador2 <=3:
        if contador1 > 0 and contador2 > 0:
            calculo = 0  #lista[cont1 -1][cont2] * lista[cont1][cont2-1]
            coluna.append(calculo)
            lista.append(coluna.copy())
            
        #end if
        contador2 += 1
    
    #endwhile    
    contador1 += 1
    contador2 = 0
#endwhile
# print(lista)
# print(lista[contador1])
# print(lista[contador2])

print('-=' * 50)

# for l in range(0,4):
#     for c in range(0,4):
#         print(f'{lista[l][c]}', end='')
#     print()  
