cont = 2000000
primo = False
i = 2
soma = 0 


    


while i != cont:

    if i % 2 == 0 and i != 2: 
        primo = False
            
    elif i  % 3 == 0 and i != 3:
        primo = False
            
    elif i % 5 == 0 and i != 5:
      primo = False
        
    elif i % 7 == 0 and i != 7:
        primo = False
        
    elif i == 2 or i == 3 or i == 5 or i == 7:
        primo = True
    else:
        primo = True
     
    if primo == True:
        soma = soma + i
        print(i)
    i = i + 1


print(f' a soma é {soma}')
