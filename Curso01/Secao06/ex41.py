soma = 0 
multiplicacao = 0 
executar  = True
resistencia = 0

while executar == True:
    r1 = input('digite o R1 ')
    if r1.isdigit():
        r1 = int(r1)
        
        r2 = input('digite o R2 ')
        if r2.isdigit() :
            r2 = int(r2)
        
            soma = r1 + r2
            
            if soma != 0:
                
           
                multiplicacao = r1 * r2
                resistencia = multiplicacao / soma

                print(f' {multiplicacao} / {soma} = {resistencia}')
            else:
                executar = False
                print(' a resistencia deu 0')
        else:
            executar = False
            print('digite um numero válido')
    else:
        executar = False
        print(' digite um numero válido')