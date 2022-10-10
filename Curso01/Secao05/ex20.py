ladoA = float(input('digite o lado A '))
ladoB = float(input('digite o lado B '))
ladoC = float(input('digite o lado C '))

if ladoA < (ladoB + ladoC) and ladoB <(ladoA + ladoC) and ladoC <(ladoA + ladoB):
    if ladoA == ladoB == ladoC:
        print(' este é um triangulo equilatero')
    
    elif ladoA == ladoB != ladoC or ladoA == ladoC != ladoB or ladoB == ladoC != ladoA:
        print(' este é um triangulo isócles')

    # usar and e deixar mais clean mais explicito
    
    elif ladoA != ladoB != ladoC != ladoA:
        print(' este é um triangulo escaleno')
    
