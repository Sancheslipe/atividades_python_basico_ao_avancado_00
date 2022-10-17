from typing import Counter
vetor = []
num = 0 
cont = 1
numRepetido = []
numerosSemRepeticao = []
while cont <= 10:
    num = input('digite um numero')
    if num.replace(".", "", 1).replace("-", "").isdigit():
        cont += 1 
        vetor.append(str(num))
    else:
        cont = cont
        print(' digite um nmero válido')
res = Counter(vetor)
numRepetido = dict(res)

if len(numRepetido) >=1:
    print(f'os numeros que não repetem são :')
    
    for chave in numRepetido:
        
        if numRepetido[chave] ==1:
            numerosSemRepeticao.append(chave)

    print(numerosSemRepeticao)

