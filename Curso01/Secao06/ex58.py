a = input('digite um numero ')
if a.isdigit():
    a = int(a)
    
    b = input('digite um numero')
    if b.isdigit():
        b = int(b)
    
    
        cont = 0
        primo = False
        soma = 0


            


        for i in range(a,b + 1):

            if i % 2 == 0 and i != 2 and i: 
                primo = False
                    
            elif i  % 3 == 0 and i != 3:
                primo = False
                    
            elif i % 5 == 0 and i != 5:
                primo = False
                
            elif i % 7 == 0 and i != 7:
                primo = False
            elif i == 1:
                primo = False

            elif i == 2 or i == 3 or i == 5 or i == 7:
                primo = True
            else:
                primo = True

            if primo == True:
                soma = soma + i
                # print(i)
            i = i + 1


        print(f'a oma dos numeros primos entre A e B é {soma}')

    
    
    
    
    else:
        print('digite um numero válido')




else:
    print('digite um numero válido')




