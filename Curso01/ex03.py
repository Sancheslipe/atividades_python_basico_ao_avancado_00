def positivo_ou_negativo(num=0):
    if num >0:
        return print(1)
    elif num < 0:
        return print(-1) 
    elif num == 0:
        return print(0)



num = input('digite um numero: ')
if num.replace('-','').isdigit():
    num = int(num)
    positivo_ou_negativo(num)
else:
    print('digite um numeo válido')