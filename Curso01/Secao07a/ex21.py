A = []
B = []
numa = 0
numb = 0
calculo = 0
C = []
cont = 0

while cont <= 9:
    numa = input('digite um numero inteiro ')
    if numa.isdigit():
        numa = int(numa)
        A.append(numa)

        numb = input('digite um numero inteiro')
        if numb.isdigit():
            numb = int(numb)
            B.append(numb)

            calculo = A[cont] - B[cont] 
            print(calculo)

            C.append(calculo)

            cont += 1

        
        
        else:
            cont = cont
            print(' digite um numero válido')
    else:
        cont = cont
        print('digite um numero válido')

print(C)