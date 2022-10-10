soma = 0 
cont = 0
num = 1

while cont < 50:
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
    num = num +1

print(f'{soma} é a soma dos primeiro {cont} numeros pares')