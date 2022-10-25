matriz1 = [[],[]]
coluna = []
matriz2 = [[],[]]
matriz3 = [[],[],[]]
Constante = 0
num = 0.0
line = 0
col = 0
cont = 0
opcao = ''
subtracao = 0
soma = 0






while line <2:
    while col <2:
        num = input(f'digite um numero referente á posição {line},{col} na primeira matriz  ')
        if num.replace('.','', 1).replace('-','').isdigit():
            coluna.append(float(num))
            matriz1[line].append(coluna[:])
            coluna.clear()
            col+=1
        
        else:
            col = col
            print('digite um numero válido')
    line+=1
    col = 0

line = 0
col = 0

while line <2:
    while col <2:
        num = input(f'digite um numero referente á posição {line},{col} na Segunda matriz  ')
        if num.replace('.','', 1).replace('-','').isdigit():
            coluna.append(float(num))
            matriz2[line].append(coluna[:])
            coluna.clear()
            col+=1
        
        else:
            col = col
            print('digite um numero válido')
    line+=1
    col = 0

print(' digite [A] para somar as duas matrizes\n digite [B] para subtrair a primeira matriz da segunda\n digite [C] para adicionar uma constante às duas matrizes\n digite [D] para imprimir as Matrizes\n')
opcao = input('digite aqui a sua opção: ')


while cont <1:
    if opcao.upper() == 'A':
        cont += 1
        print('você escolheu a opção A')
        for l in range(0,3):
            for c in range(0,3):
                if l < 2:
                    if c < 2:
                        soma = matriz1[l][c][0] + matriz2[l][c][0]
                        matriz3[l].append(soma)
                    else:
                        matriz3[l].append(0)
                else:
                    matriz3[l].append(0)

        print(f'matriz 3')
        for l in range(0,3):
            for c in range(0,3):
                print(f'[{matriz3[l][c]:}]', end= ' ,')
            print()
             

    
    
    
    elif opcao.upper() == 'B':
        cont += 1
        print('você escolheu a opção [B]')

        for l in range(0,3):
            for c in range(0,3):
                if l < 2:
                    if c < 2:
                        subtracao = matriz2[l][c][0] - matriz1[l][c][0]
                        matriz3[l].append(subtracao)
                    else:
                        matriz3[l].append(0)
                else:
                    matriz3[l].append(0)

        print(f'matriz 3')
        for l in range(0,3):
            for c in range(0,3):
                print(f'[{matriz3[l][c]:}]', end= ' ,')
            print()
    
    
    
    
    elif opcao.upper() == 'C':
        cont += 1
        print('você escolheu a opção [C]')
        
        cont = 0
        while cont <1:
            Constante = input('digite o valor da constante')
            if Constante.replace('.','', 1).replace('-','').isdigit():
                cont += 1
                Constante = float(Constante)

                for l in range(0,2):
                    for c in range(0,2):
                        matriz1[l][c] = matriz1[l][c][0] + Constante
                        matriz2[l][c] = matriz2[l][c][0] + Constante

                print(f'matriz 1')
                for l in range(0,2):
                    for c in range(0,2):
                        print(f'{matriz1[l][c]}', end= ' ')
                    print()
            
                print(f'matriz 2')
                for l in range(0,2):
                    for c in range(0,2):
                        print(f'{matriz2[l][c]}', end= ' ')
                    print()

            else:
                cont = cont
                print('digite um valor valido para a constante')




    elif opcao.upper() == 'D':
        cont += 1
        print('você escolheu a opção [D]')


        print(f'matriz 1')
        for l in range(0,2):
            for c in range(0,2):
                print(f'{matriz1[l][c]}', end= ' ')
            print()
        
        print(f'matriz 2')
        for l in range(0,2):
            for c in range(0,2):
                print(f'{matriz2[l][c]}', end= ' ')
            print()
    else:
        cont = cont
        print('digite uma opçção válida')