vetor = []
num = 0
cont = 1

while cont<= 10:
    num = input('Digite um Numero real')
    if num.replace('.','', 1).replace('-','').isdigit():
        num = float(num)
        vetor.append(num)
        cont +=1
    else:
        cont = cont
        print('digite um numero válido')

vetor.sort()
print(vetor)