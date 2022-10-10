
stop = False
dadosLidos = 0 
valoresPares = 0

while stop == False :
    
    num = int(input(' Digite um numero inteiro'))
    dadosLidos = dadosLidos +1
    
    if num != 1000:
        
        if num % 2 == 0:
            valoresPares = valoresPares + 1 
            print(f'o numero {num} é par')

        else:
            print(f'o numero {num} é impar')
    else:
        stop = True
    
    
print(f'O Numero de dados lidos é {dadosLidos}\nO numero de valores pares lidos é {valoresPares}')

