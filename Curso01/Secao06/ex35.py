valorInicial = input('digite o valor inicial')
soma = 0 
i = 0
if valorInicial.isnumeric():
    valorInicial = int(valorInicial)
    
    valorFinal = input('digite o valor Final')

    if int(valorFinal) == int(valorInicial):
        print('digite valores ')
    elif (valorFinal.isnumeric()) and valorInicial < int(valorFinal) :
        valorFinal = int(valorFinal)

        if (valorInicial + 1) % 2 == 0:
            i = 2
            for n in range(valorInicial , valorFinal, 2):
                print(n)
                soma = soma + n
        
        
        else:#(valorInicial + 1) % 2 != 0
            i = 2
            for n in range(valorInicial +1, valorFinal, i):
                print(n)
                soma = soma + n

         

        print(f' aq soma dos impares dos intervalos é {soma}')
    else:
        print(f'intervalo de valores inválido')
else:
    print('digite um numero válido')

