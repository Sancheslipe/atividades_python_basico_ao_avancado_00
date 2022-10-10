num1 = int(input('digite o numero 1 '))
num2 = int(input('digite o numero 2 '))
num3 = int(input('digite o numero 3 '))

if num1 > num2 and num2 > num3:
    print(f'{num1} , {num2} , {num3}')

elif num1 > num3 and num3 > num2:
    print(f'{num1} , {num3} , {num2}')

elif num2 > num1 and num1 > num3:
    print(f'{num2} , {num1} , {num3}')

elif num2 > num3 and num3 > num1:
    print(f'{num2} , {num3} , {num1}')

elif num3 > num2 and num2 > num3:
    print(f'{num3} , {num1} , {num2}')

elif num3 > num2 and num2 > num1:
    print(f'{num3} , {num2} , {num1}')
