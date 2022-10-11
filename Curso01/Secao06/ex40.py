
maior = 0
menor = 999999999999999999999
executar = True

while executar  == True:
    num = input('digite um numero inteiro!')
    if num.isdigit():
        num = int(num)
        
        if num > maior:
            maior = num
            
        if num < menor:
            menor = num
            
        if num < 0 :
            executar = False
                
    else:
        executar  = False
        print(' digite um numero vàlido')

print(f'o maior numero é {maior} o menor numero é {menor}')