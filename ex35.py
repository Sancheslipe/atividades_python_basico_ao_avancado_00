dia = int(input('digite o numero do dia'))
mes = int(input('digite o numero referenta ao mês '))
ano = int(input('digite o ano'))
dataValida = False
if mes == 1 and dia >= 1 and dia<=31  :
    dataValida = True
    
elif mes == 2 : 
    if ano % 4 == 0 and ano %100 != 0 or ano % 400 == 0 and dia >= 1 and dia <=29 :
        dataValida = True
    elif ano % 4 != 0 and ano %100 == 0 or ano % 400 != 0 and dia >= 1 and dia <=28 :
        dataValida = True
       
elif mes == 3 and dia >= 1 and dia<=31  :
    dataValida = True

            
elif mes == 4 and dia >= 1 and dia<=30  :
    dataValida = True

                
elif mes == 5 and dia >= 1 and dia<=31  :
    dataValida = True    
elif mes == 6 and dia<=30  :
    dataValida = True
                        
elif mes ==7 and dia >= 1 and dia<=31 :
    dataValida = True

if mes == 8 and dia >= 1 and dia<=31  :
    dataValida = True
    
elif mes == 9 and dia >= 1 and dia<=30  :
    dataValida = True
        
elif mes == 10 and dia >= 1 and dia<=31  :
    dataValida = True
            
elif mes == 11 and dia >= 1 and dia<=30  :
    dataValida = True
                
elif mes == 12 and dia >= 1 and dia<=31  :
    dataValida = True

if dataValida == True:
    print( 'Data Válida')
else:
    print('data Inválida')