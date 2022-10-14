mediaGeral = 0
mediaResidencial = 0
somaResidencial = 0
totalResidncial = 0
mediaComercial = 0
somaComercial = 0 
totalComercial = 0
mediaIndustrial = 0
somaIndustrial = 0
totalIndustrial = 0
valorKwh = 0
consumoMes = 0 
codigoConsumidor = ''
cont = 1
maiorUnidade = ''
menorUnidade = ''
maior = 0
menor = 999999999999999999999999999


habitantes = input('digite o numero de habitante')
if habitantes.isdigit():
    habitantes = int(habitantes)
    print(habitantes)

    valorKwh = input('digite o valor do Kilowatt hora')
    if  valorKwh.replace(".", "", 1).isdigit():
        valorKwh = float(valorKwh)

        while cont <= habitantes:
            print('digite o numero correspondente ao seu código de consumidor!\n 1 - Residencial,\n 2 - Comercial,\n 3 - Industrial')  
            codigoConsumidor = input('digite aqui sua area   ')

            
            if codigoConsumidor =='1':
                
                consumoMes = input('digite o seu consumo de energia por mes')
                
                if consumoMes.replace(".", "", 1).isdigit():
                    
                    consumoMes = float(consumoMes)
                    somaResidencial = somaResidencial + consumoMes 
                    cont = cont +1   
                else:
                    print('digite um numero válido')
            
            
            elif codigoConsumidor =='2':
                
                consumoMes = input('digite o seu consumo de energia por mes')
                
                if consumoMes.replace(".", "", 1).isdigit():
                    
                    consumoMes = float(consumoMes)
                    somaComercial = somaComercial + consumoMes
                    cont = cont +1    
                else:
                    print('digite um numero válido')
            
            
            elif codigoConsumidor =='3':
                
                consumoMes = input('digite o seu consumo de energia por mes')
                
                if consumoMes.replace(".", "", 1).isdigit():
                    
                    consumoMes = float(consumoMes)
                    somaIndustrial = somaIndustrial + consumoMes
                    cont = cont +1    
                else:
                    print('digite um numero válido')




        if (somaResidencial > somaComercial) and (somaComercial > somaIndustrial):
            maior = somaResidencial
            maiorUnidade = 'Unidade Residencial'
            menor = somaIndustrial
            menorUnidade = 'Unidade Industrial'
        
        elif(somaResidencial > somaIndustrial) and (somaIndustrial > somaComercial):
            maior = somaResidencial
            maiorUnidade = 'Unidade Residencial'
            menor = somaComercial
            menorUnidade = 'Unidade Comercial'
        
        elif (somaComercial > somaResidencial) and (somaResidencial > somaIndustrial):
            maior = somaComercial
            maiorUnidade = 'Unidade Comercial'
            menor = somaIndustrial
            menorUnidade = 'Unidade Industrial'
        
        elif(somaComercial > somaIndustrial) and (somaIndustrial > somaResidencial):
            maior = somaComercial
            maiorUnidade = 'Unidade Comercial'
            menor = somaResidencial
            menorUnidade = 'Unidade Residencial'
        
        elif (somaIndustrial > somaComercial) and ( somaComercial > somaResidencial):
            maior = somaIndustrial
            maiorUnidade = 'Unidade Industrial'
            menor = somaResidencial
            menorUnidade = 'Unidade Residencial'
        
        elif(somaIndustrial > somaResidencial) and (somaResidencial > somaComercial):
            maior = somaIndustrial
            maiorUnidade = 'Unidade Industrial'
            menor = somaComercial
            menorUnidade = 'Unidade Comercial'

        
        mediaGeral = (somaComercial + somaIndustrial + somaResidencial) / habitantes
        mediaResidencial = somaResidencial / habitantes
        mediaComercial = somaComercial / habitantes
        mediaIndustrial = somaIndustrial / habitantes
        
        totalResidencial = somaResidencial * valorKwh
        totalComercial = somaComercial * valorKwh
        totalIndustrial = somaIndustrial * valorKwh



        print(f' a maior unidade consumidora é {maiorUnidade} consumindo {maior} KwH')
        print(f' a menor unidade consumidora é {menorUnidade} consumindo {menor} KwH')
        
        print(f' a media geral de consumo por habitantes é {mediaGeral}')
        
        print(f' a media de consumo Residencial é {mediaResidencial}')
        print(f' a media de consumo Comercial é {mediaComercial}')
        print(f' a media de consumo Industrial é {mediaIndustrial}')

        print(f' o total do consumo da Unidade Residencial é {totalResidencial}')
        print(f' o total de consumo da Unidade Comercial é {totalComercial}')
        print(f' o total de consumo da Unidade Industrial é {totalIndustrial}')


    else:

        print('digite um valor válido')
else:
    print('digite um numero de habitantes válido')
   