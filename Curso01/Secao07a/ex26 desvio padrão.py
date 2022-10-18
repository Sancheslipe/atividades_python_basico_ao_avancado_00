V = [] #vetor
num = 0
cont = 1
DesvioPadrao = 0
somaVariancia = 0
somaSimples = 0
mediaSimples = 0


while cont <=10:
    num = input('digite um numero')
    if num.replace('.', '', 1).replace('-', '').isdigit():
        cont += 1
        num = float(num)
        V.append(num)
    else:
        cont = cont
        print('digite um numero válido')

for i in range(0,len(V)):
    somaSimples += V[i]


mediaSimples = somaSimples / len(V)

for i in range(0,len(V)):
    somaVariancia += (V[i] - mediaSimples) ** 2



variancia = somaVariancia / len(V)
DesvioPadrao = variancia ** 0.5
print(f' a media simples é {mediaSimples}, a Variancia é {variancia}, e o desvio padrão é {DesvioPadrao} ')

#teste feito com 6 (cont <=6) numeros sendo eles 5,8,4,9,9,7 Variancia == raiz de 3,6
#busquei uma ajuda no canal de matemática professor marcos Aba para entender melhor o calculo