list=[]
cont= 1
while cont <= 6:
    num = input('digite um numero')
    if num.isdigit():
        num = int(num)
        list.append(num)
        cont = cont + 1
    else:
        print('digite um numero válido')
        cont = cont

print(list)