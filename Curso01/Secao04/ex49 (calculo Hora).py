hora = int(input('digite qual a hora que começou o experimento ( em horas)'))
minuto = int(input('digite qual o minuto que comecou o experimento (em Minutos)'))
segundo = int(input('digite qual o segundo que começou o experimento(em segundos)'))

duracao = int(input('digite qual foi o tempo de duração do experimento (em segundos)'))

segundosTotais = (hora * 3600) + (minuto * 60) + segundo + duracao

horaFinal = segundosTotais // 3600 
coeficiente = segundosTotais % 3600
minutosFinais = coeficiente // 60
segundosFinais = coeficiente % 60


print(f' o experimento acabou às {horaFinal}:{minutosFinais} e .{segundosFinais} segundos')