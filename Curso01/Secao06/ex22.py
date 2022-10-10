notasValidas = True
quantidadeNotas = 0
mediaAritmetica = 0
somaNota = 0

while notasValidas == True:
    notas = input('Digite as notas ')
    
    if notas.isdigit():
        notas = float(notas)
    else:
        print('digite uma nota válida') 
        notasValidas == False
        quit()

    if notas >=10 and notas <= 20:
        notasValidas = True
        quantidadeNotas = quantidadeNotas + 1
        somaNota = somaNota + notas
    else:
        notasValidas = False

mediaAritmetica = somaNota  / quantidadeNotas

print(f' a média final é {mediaAritmetica}')

    # Válidação de número 
    # if var(do tipo string).isdigit():
    #     notas = float(notas)
    # else:
    #     print('digite uma nota válida') 

    #     quit()