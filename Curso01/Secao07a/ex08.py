vetor = []
num = 0
cont = 1

while cont <= 6:
    num = input('digite um numero inteiro')
    if num.isdigit():
        vetor.append(int(num))
        cont += 1


    else:
        cont = cont
        print('digite um numero válido')
print(vetor[:: -1])