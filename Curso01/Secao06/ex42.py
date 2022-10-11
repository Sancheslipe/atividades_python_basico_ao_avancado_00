quadrado = 0 
cubo = 0
raizQuadrada = 0
executar = True

while executar  == True:
    val = input(' digite um valor')
    if val.isdigit():
        if int(val) != 0:
            val = int(val)
            
            quadrado = val ** 2
            cubo = val ** 3
            raizQuadrada = val ** 0.5
            print(f' o quadrado do numero é {quadrado}\no cubo do numero é {cubo}\na raiz quadrada do numero é {raizQuadrada}')
        else:
            executar = False
    else:
        executar = False
        print('digite um numero válido')
