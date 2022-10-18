vetor1 = []
vetor2 = []
tamanho = 0
mult = 0
num = 0
dif = 0
inter = 0
soma = 0
cont = 1
uni = 0

while cont <= 10:
    num = input('Digite um numero inteiro')
    if num.isdigit():
        num = int(num)
        if cont<= 5:
            vetor1.append(num)
        else:
            vetor2.append(num)

        cont += 1
    else:
        cont = cont
        print('digite um numero válido')



for i in range(0, 5):
    soma = soma +(vetor1[i] + vetor2[i])
    mult += vetor1[i] * vetor2[i]

dif = set(vetor1).difference(set(vetor2))
inter = set(vetor1).intersection(set(vetor2))
uni = set(vetor1).union(set(vetor2))




print(f' esta é a soma {soma},\n esta é a multiplicação {mult},\n esta é a diferença {dif}, \n esta é a intersecção {inter}, \n esta é a união{uni}')