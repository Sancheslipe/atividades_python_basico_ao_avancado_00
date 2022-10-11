num = int(input('digite um numero'))
fibonacci = []
cont = 0
antecessor = 0
sucessor = 1
executar = True
while antecessor< num   :
    fibonacci.append(str(antecessor))
    fibonacci.append(str(sucessor))
    antecessor = antecessor + sucessor
    sucessor = sucessor + antecessor
    cont = cont + 1
    if cont == 10:
        executar  = False    

print(fibonacci)