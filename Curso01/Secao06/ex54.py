num = input('digite um numero')
if (num.isdigit()) and (int(num) > 0):
    
    num = int(num)
    
    if num % 2 == 0 and num != 2: 
        print('este numero não é primo!')
    
    elif num  % 3 == 0 and num != 3:
        print(' não é primo')
    
    elif num % 5 == 0 and num != 5:
        print(' este numero não é primo!')
   
    elif num % 7 == 0 and num != 7:
        print('Este numero não é primo!')
    
    else:
        print('este numero é primo!')
else:
    print('digite um numero válido')