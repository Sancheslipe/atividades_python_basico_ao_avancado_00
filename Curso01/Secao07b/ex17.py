matriz = []
coluna = []
notas = []
nota = 0
nota1 = 0
nota2 = 0
nota3 = 0
line = 0
col = 0 

while line < 10:

    while col<3:        
        
        nota  = input(f' digite sua {col+1}° nota ')
        if nota.replace('.','', 1).isdigit():
            coluna.append(float(nota))
            matriz.append(coluna[:])
            col += 1
        
            coluna.clear()
        else:
            col = col 
            print(f' digite um numero válido !')

    
    line += 1
    col = 0    

    if matriz[0] < matriz[1] and matriz[1] < matriz [2]:
        nota1 += 1
    elif matriz[0] < matriz[2] and matriz[2] < matriz[1]:
        nota1 +=1

    elif matriz[1] < matriz[0] and matriz[0] < matriz[2]:
        nota2 +=1
    elif matriz[1] <matriz[2] and matriz[2] <matriz[0]:
        nota2 +=1
        
    elif matriz[2] < matriz[0] and matriz[0] < matriz[1]:
        nota3 +=1
    elif matriz[2] <matriz[1] and matriz[1] < matriz[0]:
        nota3 +=1
            
            #se for igual
    elif matriz[0] > matriz[1] and matriz[2] == matriz [1]:  
        nota2 +=1
            
    elif matriz[1] > matriz[0] and matriz[0] == matriz [2]:
        nota1 += 1
        
    elif matriz[2] > matriz[1] and matriz[1] == matriz [0]:
        nota3 +=1
    
    matriz.clear()                
            
   
    
matriz.append(nota1)
matriz.append(nota2)
matriz.append(nota3)



for l in range(0,3):
    print(f' o numero de pessoas que tem a nota {l +1} mais baixa é')
    print(f'{matriz[l]}', end=' ')
    print()