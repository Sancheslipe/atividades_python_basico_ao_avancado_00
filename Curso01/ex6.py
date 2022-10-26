def conversor_segundos(hora, minuto, segundo):
    
    segundosTotais = ((int(hora) * 3600) + (int(minuto) * 60) + int(segundo) )
    return segundosTotais


hora = input('digite a hora: ')
if hora.isdigit():
    hora = int(hora)
    minuto = input('digite os minutos: ')
    if minuto.isdigit():
        minuto = int(minuto)
        segundo = input(' digite os segundos: ')
        if segundo.isdigit():
            segundos = int(segundo)
            
            print(f'os segundos totais são {conversor_segundos(hora,minuto,segundo)}')

        else:
            print('digite um segundo válido')    

    else:
        print('digite um minuto válido')

else:
    print('digite uma hora válida')
