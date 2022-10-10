num = input('digite um numero')
cont = 1
divisores =  [] 
if num.isdigit() == True:
    num = int(num)

else:
    print('digite um numero')


while cont <= num:
    if num % cont == 0:
        divisores.append(str(cont))
    cont += 1

print(f'Estes são os divisores {divisores}')