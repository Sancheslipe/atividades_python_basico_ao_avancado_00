vetor = []
vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []
vetor5 = []
numerosImpares = []
num = 0 

for i in range(0,50):
    
    if i <= 9:
        vetor1.append(i)
    elif i >9 and i <=19:
        vetor2.append(i)
    elif i >19 and i <=29:
        vetor3.append(i)
    elif i >29 and i <=39:
        vetor4.append(i)       
    elif i >39 and i <=49:
        vetor5.append(i)


vetor.append(vetor1)
vetor.append(vetor2)
vetor.append(vetor3)
vetor.append(vetor4)
vetor.append(vetor5)

for indice, valor in enumerate(vetor):# 0 , 1, 2,3 ,4  | 0[], 1[],2[],3[],4[]
    for i, v in enumerate(vetor[indice]):#para indice e valor dentro do vetor no indice1
        
        if v % 2 != 0:
            numerosImpares.append(v)    
        else:
            numerosImpares.append(None)
        
        print(f'vetor 1| {v}', end= " ")
        print(f'vetor 2| {numerosImpares[v]}')