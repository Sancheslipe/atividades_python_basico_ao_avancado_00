vetor = []
ordemCerta =[]
num = 0
cont = 1
#verificando se é um numero real e apendendo ele dentro de um vetor
while cont<= 11:
    num = input('Digite um Numero real')
    if num.replace('.','', 1).replace('-','').isdigit():
        num = float(num)
        vetor.append(num)
        cont +=1
    else:
        cont = cont
        print('digite um numero válido')
#organizando o vetor principal
vetor.sort()
#adicionando na ordem comum até o index 4
for i in range(0,5):
    ordemCerta.append(vetor[i])
# adicionando na ordem invertida, do index 10 até o index 5
for i in range(10, 4, -1):
    ordemCerta.append(vetor[i])
#printando a certa
print(ordemCerta)

