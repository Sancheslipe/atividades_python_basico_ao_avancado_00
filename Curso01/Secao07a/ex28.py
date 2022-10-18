vetor = []
v1Impar = []
v2Par = []
num = 0
cont = 1

while cont <= 10:
    num = input('Digite um Numero')
    if num.isdigit():
        num = int(num)
        vetor.append(num)
        cont += 1  
    else:
        cont = cont
        print(' digite um numero válido')

for i in range( 0, len(vetor)):
    if vetor[i] % 2 == 0:
        v2Par.append(vetor[i])
    else:
        v1Impar.append(vetor[i])
    

print(f'Os elementos utilizados em V1 e V2 foram {v1Impar}, {v2Par}')
