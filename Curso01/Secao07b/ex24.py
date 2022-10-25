import random
matriz = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] 
coluna = []
diagonal = 0
diagonalInversa = 0
horizontal = 0
vertical = 0
num = 0
maior = 0
maiores =''
maiorOperacao = ''
A = B = C = D = 0

for l in range(0,20):
    for c in range(0,20):
        num = int(random.randint(1, 99))


        matriz[l].append(num)



for l in range(0,20):
    for c in range(0,20):
        print(f'  {matriz[l][c]:}', end = '  ')
    print()

#para achar o adjacente é só faz

#METODO DIAGONAL
for l in range(0,10):
    for c in range(0,10):
        if l <=16 and c <=16:
            A = B = C = D = 0

            A = matriz[l][c]
            
            B = matriz[l+1][c+1]
            
            C = matriz[l+2][c+2]
            
            D = matriz[l+3][c+3]

            diagonal = A * B * C * D

            if diagonal > maior:
                maiorOperacao = 'diagonal'
                maior = diagonal
                maiores = A , B , C, D


# # #METODO HORIZONTAL

        if l <= 16 and c <= 16:
            
            A = B = C = D = 0

            A = matriz[l][c]
            
            B = matriz[l][c+1]
            
            C = matriz[l][c+2]
            
            D = matriz[l][c+3]
            
            horizontal = A * B * C * D

        if horizontal > maior:
            maiorOperacao = 'horizontal'
            maior = horizontal
            maiores = A , B , C, D



# # #METODO Vertical
        

        if l <=16 and c <=16:
            A = B = C = D = 0

            A = matriz[l][c]
            
            B = matriz[l+1][c]
            
            C = matriz[l+2][c]
            
            D = matriz[l+3][c]

            vertical = A * B * C * D

            if vertical > maior:
                maiorOperacao = 'vertical'
                maior = vertical
                maiores = A , B , C, D

        

# # #METODO DIAGONAL INVERSA

        if l <=16 and c <=16:
            A = B = C = D = 0

            A = matriz[l][c]
            
            B = matriz[l+1][c-1]
            
            C = matriz[l+2][c-2]
            
            D = matriz[l+3][c-3]

            diagonalInversa = A * B * C * D

            if diagonalInversa > maior:
                maiorOperacao = 'diagonalINversa'
                maior = diagonalInversa
                maiores = A , B , C, D
           

        
print(F' A maior operação foi {maiorOperacao} ESTE É O maior numero {maior}\n e os numeros que geraram foram {maiores}')
                        



            

            
                
 
