vetor = []
impares = []
pares = []
num = 0
cont = 1
contImpar = 0

while cont<=6:
    num = input('digite um numero inteiro')
    if num.isdigit():
        num = int(num)
        vetor.append(num)
        cont += 1
    else:
        cont = cont
        print('digite um numero válido')

for i in range(0,len(vetor)):
    if vetor[i] % 2 ==0:
        pares.append(vetor[i])
    else:
        impares.append(vetor[i])
        contImpar += 1

print(f' Os numeros pares digitados foram {pares}, e a soma deles é {sum(pares)}\n Os numeros impares digitados foram{impares}, e a quantidade de numeros impares digitados foi {contImpar} ')