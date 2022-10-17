cont = 1
numReais = []
raizQuadrada = []

while cont <= 10:
    num = input('digite um numero')


    if num.replace(".", "", 1).isdigit():
        num = float(num)
        numReais.append(num)
        raizQuadrada.append( num **2)

    
    
    
        cont = cont + 1
    else:
        print('Digite um numero válido')
        cont = cont



print(raizQuadrada)
print(numReais)