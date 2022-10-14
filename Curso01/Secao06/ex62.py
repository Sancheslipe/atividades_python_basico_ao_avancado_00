cont = 1
num = ''
totalLetras = 0
executar = True
print(len(num))

while executar == True:
    if cont <=5: # esta logica está aplicada para 5 numeros para que o teste seja mais rápido e prático , caso queira com 1000 só trocar o parametro do 1 IF
        num = input(f'digite o numero {cont} por extenso\n')
        
        if (' 'not in num) and ('-' not in num):
            totalLetras += len(num)
            cont += 1
        
        else:
            print('digite o numero sem dar espaço ou hífen')
            cont = cont
        

    else:
        executar  = False
    
print(f' o total de Letras é {totalLetras}')    

