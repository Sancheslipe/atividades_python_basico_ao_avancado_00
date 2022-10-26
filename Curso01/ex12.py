def soma_algarismos(numero):
    numero = int(numero)
    somaAlgarismo = 0 
    for c in range(0, numero + 1):
        somaAlgarismo = somaAlgarismo + int(str(num)[c])

    print(somaAlgarismo)

num = int(input('digite um numero'))
soma_algarismos(num)
    
