vetor = []
indexPrimos = []
primos = []
num = 0
cont = 1

while cont<= 10:
    num = input('digite um numero ')
    if num.isdigit():
        num = int(num)
        vetor.append(num) 
        cont += 1        
    else:
        cont = cont
        print('digite um numero válido')

for i in range(0, len(vetor)):
    if (vetor[i] != 2) and (vetor[i] % 2 == 0):
        i = i
    elif (vetor[i] !=3) and (vetor[i] %3 == 0):
        i = i
    else:
        indexPrimos.append(i)
        primos.append(vetor[i])


        
print(f' o index dos primos são {indexPrimos}, e os numeros primos são {primos}')





