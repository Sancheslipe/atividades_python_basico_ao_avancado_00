
num1 = input('digite um numero')

cont = 1
diferenca = 0 
intervalo = 0
impar = 1
par = 0

#Validande se é um numero mesmo 
if num1.isdigit():
    num1 = int(num1)
else:
    print('digite um numero inteiro')

num2 = input('digite um numero')

if num2.isdigit():
    num2 = int(num2)
else:
    print('digite um numero inteiro')

#vendo qual é o numero maior para não dar intervalo negativo

if num1 > num2:
    diferenca = num1 - num2
    
    while cont <= diferenca:
        intervalo = num2 + cont
        if intervalo % 2 == 0 :
            par = par + intervalo       
        else:
            impar = impar * intervalo
        cont = cont + 1
elif num2 > num1:
    diferenca = num2 - num1
    
    while cont <= diferenca:
        intervalo = num1 + cont
        if intervalo % 2 == 0 :
            par = par + intervalo
        else:
            impar = impar * intervalo
        cont = cont +1

print(f'a soma dos pares deu {par} e a multiplicação dos impares deu {impar} ')

