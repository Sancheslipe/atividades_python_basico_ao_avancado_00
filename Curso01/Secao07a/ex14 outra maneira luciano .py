from typing import Counter
vetor = []
num = 0 
cont = 1
cont2 = 0
numRepetido = []
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
    print(f'Temos numeros repetidos!')
    for chave in numRepetido:
        if numRepetido[chave] >=2:
            print(f'o numero {chave} repete {numRepetido[chave]} vezes')
else:
    print('não tem numeros repetidos')




