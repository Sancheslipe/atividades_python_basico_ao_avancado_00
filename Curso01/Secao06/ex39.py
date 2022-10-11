base = input('digite a base')

if base.isdigit() and (int(base) > 0 or int(base) != 0  ):
    base = int(base)

    altura = input('digite a altura')
    
    if altura.isdigit() and (int(altura) > 0 or int(altura) != 0  ):
        altura = int(altura)
        calculo = (base * altura) / 2 

        print(f' a área do triangulo é {calculo}')
    
    
    
    else:
        print('digite um numero válido')
else:
    print('digite um numero válido')
