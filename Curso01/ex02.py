
def data_extenso(dia,mes,ano):
    if mes == 1:
        mesExtenso = 'janeiro'
    elif mes == 2:
        mesExtenso = 'fevereiro'
    elif mes == 3:
        mesExtenso = 'março'
    elif mes == 4:
        mesExtenso = 'abril'
    elif mes == 5:
        mesExtenso = 'maio'
    elif mes == 6:
        mesExtenso = 'junho'
    elif mes == 7:
        mesExtenso = 'julho'
    elif mes == 8:
        mesExtenso = 'agosto'
    elif mes == 9:
        mesExtenso = 'setembro'
    elif mes == 10:
        mesExtenso = 'outubro'
    elif mes == 11:
        mesExtenso = 'novembro'
    elif mes == 12:
        mesExtenso = 'dezembro'


    data_extenso = f'{dia} de {mesExtenso} de {ano}'
    return data_extenso


bissexto = False
ano = input('digite o ano: ')
if ano.isdigit():
    ano = int(ano)
    
    if (ano % 4 == 0) and (ano % 100 == 0) and (ano % 400 == 0):
        bissexto = True 

   
    mes = input('digite o mes em numero: ')
    
    if (mes.isdigit()) and (int(mes)>=0 and int(mes) <=12):
       
        mes = int(mes)  
        
        dia = input('digite o dia: ')
        
        if (mes >= 1 and mes <= 7):
            
            if (dia.isdigit()) and (mes == 2) and (bissexto == True) and int(dia) >= 1 and int(dia) <=29:
                dia = int(dia)
                print(data_extenso(dia,mes,ano))

            elif (dia.isdigit()) and (mes == 2) and (bissexto == False) and int(dia) >= 1 and int(dia) <29:
                dia = int(dia)
                print(data_extenso(dia,mes,ano))
            
            elif (dia.isdigit()) and (mes == 2) and (bissexto == False) and int(dia) > 29:
                print('data inválida')
            elif (dia.isdigit()) and (mes == 2) and (bissexto == True) and int(dia) > 29:
                print('data inválida')

            elif (dia.isdigit()) and (mes % 2 == 0) and int(dia) >= 1 and int(dia) <=30:
                dia = int(dia)
                print(data_extenso(dia,mes,ano))

            elif (dia.isdigit()) and (mes % 2 != 0) and int(dia) >= 1 and int(dia) <=31:
                dia = int(dia)
                print(data_extenso(dia,mes,ano))

            else:
                print('digite um dia válido 1')
        
        elif (mes >= 8 and mes <= 12):
            
            if (dia.isdigit()) and (mes % 2 == 0) and int(dia) >= 1 and int(dia) <=31:
                dia = int(dia)
                print(data_extenso(dia,mes,ano))

            elif (dia.isdigit()) and (mes % 2 != 0) and int(dia) >= 1 and int(dia) <=30:
                dia = int(dia)
                print(data_extenso(dia,mes,ano))
                
            else:
                print('digite um dia válido 2')
                
                
        
        
        else:
            print('digite um numero válido3 ')

    else:
        print('digite um mês válido')


else:
    print('digite um ano válido')


