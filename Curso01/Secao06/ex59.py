from curses.ascii import isdigit


valorKwh = 0
consumoMes = 0 
codigoConsumidor = ''
cont = 1
maior = 0
menor = 999999999999999999999999999


habitantes = input('digite o numero de habitante')
if habitantes.isdigit():
    habitantes = int(habitantes)

    valorKwh = input('digite o valor do Kilowatt hora')
    if  valorKwh.replace(".", "", 1).isdigit():
        valorKwh = float(valorKwh)

        while cont <= habitantes:
            consumoMes = input('digite o seu consumo de energia por mes')
            if consumoMes.replace(".", "", 1).isdigit():
                consumoMes = float(consumoMes)

                print('digite o numero correspondente ao seu código de consumidor!\n 1 - Residencial,\n 2 - Comercial,\n 3 - Industrial')  
                codigoConsumidor = input('digite aqui sua area   ')

                if codigoConsumidor =='1':
                    print('qualquer coisa')













            else:
                print('digite um numero válido')
    else:
        print('digite um valor válido')
else:
    print('digite um numero de habitantes válido')