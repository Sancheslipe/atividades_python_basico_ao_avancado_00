num = input('digite um numero')
if num.isdigit():
    num = int(num)
    fibonacci = []
    cont = 0
    antecessor = 0
    sucessor = 1
    executar = True
    while executar == True   :
        fibonacci.append(str(antecessor))
        fibonacci.append(str(sucessor))
        antecessor = antecessor + sucessor
        sucessor = sucessor + antecessor
        if num < antecessor :
            executar  = False    
    

    print(fibonacci)
else:
    print('digite um numero válido')