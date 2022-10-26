def maior(num1,num2):
    num1 = num1 * 1
    num2 = num2 * 1
    
    if num1 > num2:
        return num1
    if num1 < num2:
        return num2
    elif num1 == num2:
        return 'ambos são iguais'
    

num1 = input(' digite o primeiro numero: ')
if num1.isdigit():
    num1 = int(num1)
    num2 = input('digite um numero referente ao segundo numero: ')
    if num2.isdigit():
        num2 = int(num2)
        
        print(f'{maior(num1,num2)}')
    
    else:
        print('digite um numero válido')
else:
    print('digite um numero válido')