quilometrosPorHora = 0
metrosPorSegundo = 0
executar  = True

while executar == True:
    print('digite o que você quer!\n [km] para converter de M/s para KM/h\n [ms] para converder de Km/h para M/s\n [quit] para fechar o programa')
    opcao = input('digite a sua resposta!     ')

    if opcao.lower() == 'km':
        velocidade = input('digit um numero real referente aos metros por segundos')

        if velocidade.replace(".", "", 1).isdigit():
            velocidade = float(velocidade)
            
            quilometrosPorHora = velocidade * 3.6
            print(f' {velocidade}M/s são {quilometrosPorHora}Km/h')


        else:
            executar = False
            print('digite um numero válido')
    elif opcao.lower() == 'ms':
            velocidade = input('digit um numero real referente aos kilometros por hora')

            if velocidade.replace(".", "", 1).isdigit():
                velocidade = float(velocidade)
                
                metrosPorSegundo = velocidade / 3.6
                print(f' {velocidade}Km/h são {metrosPorSegundo}M/s')

            else:
                executar = False
                print('digite um numero válido')
    elif opcao.lower() == 'quit':
        print('você escolheu finalizar o programa!')    
        executar = False
    else:
        print('digite uma opção válida')