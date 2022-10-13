verResultado = 0
executar  = True
adicao = 0 
subtracao = 0
multiplicacao = 0
divisao = 0 
saida  = 0
opcao = ''
resultado = 0

while executar  == True:
    print('para executar as funções abaixo, digite o numero correspondente específicado abaixo:\n [1] Adição\n [2] Subtração\n [3] Multiplicação\n [4] Divisão\n [5] saída\n')
    opcao = input('digite aqui sua opção  ')

    if opcao == '1':
            num1 = input('digite o primeiro numero para a soma')
            if num1.isdigit:
                num1 = int(num1)
                
                num2 = input('digite o segundo numero para a soma')
                if num2.isdigit():
                    num2 = int(num2)
                    adicao = num1 + num2
                    resultado = adicao
                
                    verResultado = input(' deseja ver o resultado? [S] para Sim [N] para Não')
                    
                    if verResultado.upper() == 'S':
                        print(f' O resultado é {resultado}')                    
                    elif verResultado.upper() == 'N':
                        print('você será direcionado ao menu de opções')                    

                else:
                    executar  = False
                    print('digite um numero válido')
            else:
                executar  = False
                print('digite um numero válido')
    elif opcao == '2':
            num1 = input('digite o primeiro numero para a subtração')
            if num1.isdigit:
                num1 = int(num1)
                
                num2 = input('digite o segundo numero para a subtração')
                if num2.isdigit():
                    num2 = int(num2)
                    subtracao = num1 - num2
                    resultado = subtracao

                    verResultado = input(' deseja ver o resultado? [S] para Sim [N] para Não')
                    
                    if verResultado.upper() == 'S':
                        print(f' O resultado é {resultado}')                    
                    elif verResultado.upper() == 'N':
                        print('você será direcionado ao menu de opções')

                else:
                    executar  = False
                    print('digite um numero válido')
            else:
                executar  = False
                print('digite um numero válido')
    elif opcao == '3':
            num1 = input('digite o primeiro numero para a multiplicação')
            if num1.isdigit:
                num1 = int(num1)
                
                num2 = input('digite o segundo numero para a multiplicação')
                if num2.isdigit():
                    num2 = int(num2)
                    multiplicacao = num1 * num2
                    resultado = multiplicacao

                    verResultado = input(' deseja ver o resultado? [S] para Sim [N] para Não')
                    
                    if verResultado.upper() == 'S':
                        print(f' O resultado é {resultado}')
                    elif verResultado.upper() == 'N':
                        print('você será direcionado ao menu de opções') 

                else:
                    executar  = False
                    print('digite um numero válido')
            else:
                executar  = False
                print('digite um numero válido')
    elif opcao == '4':
            num1 = input('digite o primeiro numero para a multiplicação')
            if num1.isdigit:
                num1 = int(num1)
                
                num2 = input('digite o segundo numero para a multiplicação')
                if num2.isdigit() and (int(num2) > 0 or int(num2) != 0):
                    
                    if (num2 > 0) or (num2 != 0):

                        num2 = int(num2)
                        divisao = num1 / num2
                        resultado = divisao
                        
                        verResultado = input(' deseja ver o resultado? [S] para Sim [N] para Não')
                        
                        if verResultado.upper() == 'S':
                            print(f' O resultado é {resultado}')
                        elif verResultado.upper() == 'N':
                            print('você será direcionado ao menu de opções')                    
                    else:
                        print('para ocorrer a divisão é necessário que o denominador tem que ser maior e diferente de zero!')
                else:
                    executar  = False
                    print('digite um numero válido ')
            else:
                executar  = False
                print('digite um numero válido')
    elif opcao == '5':
        verResultado = input(' deseja ver o resultado? [S] para Sim [N] para Não')
        if verResultado.upper() == 'S':
            print(f' O resultado é {resultado}')
        elif verResultado.upper() == 'N':
            print('você será direcionado ao menu de opções')
