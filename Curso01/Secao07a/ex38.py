vetor = []
num = 0 


while len(vetor) <= 9:
    num = input('Digite um valor numérico')
    if num.replace('.','', 1).replace('-','').isdigit():
        num = float(num)
        vetor.append(num)
        vetor.sort()
    else:
        cont = cont
        print('Digite um numero válido')

print(vetor)