linha = [[],[],[],[]]
coluna = []
num = 0
cont1 = 0
cont2 = 0
maiorQue10 = 0


while cont1 <=3:
    
    while cont2 <= 3:
        print(f'\n este é o index {cont1} {cont2} \n')
        num = input('digite um numero')
        if num.replace('.','' , 1).replace('-','').isdigit():
            num = float(num)
            if num > 10:
                maiorQue10 += 1
            
            coluna.append(num)
            linha[cont2].append(coluna.copy())
            
            coluna.clear()
            
                     
            
            cont2 +=1
        else:
            cont2 = cont2 
            print('digite um numero válido')        
    
    cont1 = cont1 + 1
    cont2 = 0
    


print('-='*30, '\n')
print(f' o total de numeros maiores que 10 é {maiorQue10} \n e os numeros digitados foram! ')

for l in range(0,4):
    for c in range(0,4):
        print(f'{linha[l][c]}', end=' ')
    print()