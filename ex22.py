idade = int(input('digite a sua idade em anos '))
tempoDeTrabalho = int(input('digite o seu tempo de trabalho em anos '))

if (idade >= 65) or (tempoDeTrabalho >= 30) or (idade >= 60 and tempoDeTrabalho >=25)   :
   print('você pode se aposentar')
else:
    print('você ainda não pode se aposentar')