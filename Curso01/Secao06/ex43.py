cont = 0
executar = True
media = 0 
soma = 0
while executar == True:
    idade = input('digite a sua idade')
    if idade.isdigit():
        if int(idade) != 0 :
            idade = int(idade)
            
            cont = cont + 1

            soma = soma + idade

            media = soma / cont


        else:
            executar = False
    
    else:
        executar = False



print(f' a média das idades é {media}')