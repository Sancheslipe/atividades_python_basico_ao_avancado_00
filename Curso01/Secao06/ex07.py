cont = 1 
num = 0
soma = 0

while cont <= 10:
    num = int(input('digite um numero'))
    if num > 0:
        soma = soma + num
        cont = cont + 1
    elif num < 0 :
        print('digite um numero válido')
    cont = cont

print(f' a média é {soma / 10}')