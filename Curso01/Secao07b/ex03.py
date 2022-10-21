# matrix = [[],[],[],[]] 
lista = []
coluna = []
num = 0 
cont1 = 0
cont2 = 0

while cont1 <= 3:
    while cont2 <=3:
        
        if (cont1 == 0):

            num = int(input(f'digite um numero referente á {cont1 },{cont2}  '))
            
            coluna.append(f'{cont1}')
            coluna.append(f'{cont2}')            
            coluna.append(num) 
            lista.append(coluna)
            print(lista)
        else:
            if (cont2 == 0):
                num = int(input(f'digite um numero referente á {cont1 },{cont2}  '))
                coluna.append(num)
                coluna.append(f'{cont1}')
                coluna.append(f'{cont2}')
                lista.append(coluna)

                print(lista)

                # print(f'primeira coluna horizontal cont2 {coluna}')
        #end if         
        cont2 += 1  
    # end while
    cont1 +=1
    cont2 = 0
# end while

cont1 = 0
cont2 = 0

# while cont1 <=3:
#     while cont2<=3: 
#         if cont1   
