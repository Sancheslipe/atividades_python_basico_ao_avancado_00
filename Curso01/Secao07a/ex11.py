from operator import contains


vetor = []
num = 0
cont = 1
contNegativo = 0
soma = 0

while cont <= 10:
    num = input('digite um numero real')
    if num.replace(".", "", 1).replace('-', '').isdigit():
        cont += 1 
        vetor.append(float(num))
    else:
        cont = cont
        print(' digite um numero válido')



for i in range(0, 9 + 1):
    if vetor[i] < 0:
        contNegativo += 1
    elif vetor[i] >=0:
        soma += vetor[i]

print(f' a quantidade de numeros negativos é {contNegativo} e a soma dos numeros positivos é {soma}')
