vetor = []
cont = 1

for i in range(1,9):
    num = input('digite um numero')
    vetor.append(int(num))


while cont <= 1:
    
    posicao1 = input('digite uma posição entre 1 e 8  ')
    if posicao1.isdigit() and (int(posicao1) >=0 and int(posicao1) <= 8):
        posicao1 = int(posicao1)
        posicao2 = input('digite uma posição entre 1 e 8  ')
        
        if posicao2.isdigit() and (int(posicao2) >= 1 and int(posicao2) <= 8):
            posicao2 = int(posicao2)
            cont = cont + 1

        else:
            print('digite uma posição válida')
    else:
        print('digite uma posição válida')

soma = vetor[posicao1] + vetor[posicao2]

print(soma)