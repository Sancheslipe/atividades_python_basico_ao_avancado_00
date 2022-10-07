"""
pedir hora de chegada e saida em pares e inteiros:FEITO
"""
valor1Hora = 1
valor2Horas = 2
valor3Horas = 3.40
valor4Horas = 4.80
valor5Horas = 6.80
valorAcimaDe5horas = 2.00

horaChegada = int(input('digite a hora de chegada"  '))
if horaChegada > 23:
    print(' digite uma hora válida')
else:    
    minutoChegada = int(input('digite o minuto de chegada"  '))
    if minutoChegada > 60:
        print('digite um minuto válido')
    else:
        horaSaida = int(input('digite a hora de partida"  ' ))
        if horaSaida > 23:
            print(' digite uma hora válida')
        else:
            minutoSaida = int(input('Digite o minuto de Partida!  '))
            if minutoSaida >60:
                print('digite um minuto válido')
            else:
                valorTotal = 0
                somaHora = 0

                if horaChegada > horaSaida :
                    somaHora = somaHora + 24
                    print('passou por aqui')
                    somaHora = (horaSaida + 24) - horaChegada
                else:
                    somaHora = horaSaida - horaChegada

                somaMinuto = minutoSaida - minutoChegada

                minutosTotais = ((somaHora * 60) + somaMinuto) 

                if minutosTotais <= 60 :
                    valorTotal = valor1Hora
                elif minutosTotais >=61 and minutosTotais <=120:
                    valorTotal = valorTotal + valor2Horas 
                elif minutosTotais >=121 and minutosTotais <=180:
                    valorTotal = valorTotal + valor3Horas
                elif minutosTotais >= 181 and minutosTotais <=240:
                    valorTotal = valorTotal + valor4Horas
                elif minutosTotais >= 241 and minutosTotais <= 300:
                    valorTotal = valorTotal + valor5Horas
                elif minutosTotais > 300:
                    if minutosTotais % 60 == 0:
                        minutosTotais = minutosTotais - 300 
                        valorTotal = valorTotal + (valorAcimaDe5horas * (minutosTotais / 60))
                    else:
                        minutosTotais =minutosTotais - 300 
                        valorTotal = valorTotal + (valorAcimaDe5horas * (minutosTotais + 60 / 60))   

                print(f' Valor Total R${valorTotal}')