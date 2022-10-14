executar = True
soma = 0 
quantidade = 0
media = 0
maior = 0
menor = 99999999999999999999999999
somaPar = 0
mediaPares = 0
contPar = 0





while executar  == True:
        
    num = input('digite um numero')

    if num.isdigit():
        num = int(num)
       
        if num != 0:
           

            quantidade  = quantidade + 1
            soma = soma + num
            if num % 2 == 0 :
                somaPar = somaPar + num
                contPar = contPar + 1
            
            if num > maior:
                maior = num

            if num < menor:
                menor = num
        else:
            executar = False    
        
    
    else:
        print('Digite um numero válido ')

mediaPares = somaPar / contPar
media = soma / quantidade 

print(f' a soma dos numeros digitados é {soma}')
print(f' a quantidade de numeros digitados é {quantidade}')  
print(f' a media os numeros digitados é {media}') 
print(f' o maior numero é {maior}')
print(f' o menor numero é {menor}')
print(f' a media os numeros pares é {mediaPares}')

    
