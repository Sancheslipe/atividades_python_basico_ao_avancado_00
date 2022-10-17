vetor = []
num = 0 
codigo = 0 # inteiro
cont =1
while cont <= 5:
    
    num = input('digite um numero ')
    if num.replace(",", "", 1).replace("-", "").isdigit():
        cont += 1
        vetor.append(float(num))   
    
    else:
        cont = cont
        print('digite um numero válido')
    
codigo = input(' digite [1] para mostrar na ordem direta\n digite [2] para mostrar na ordem inversa')
    
if codigo.isdigit():
    codigo = int(codigo)

    if codigo == 1:
         print(vetor)
    elif codigo ==2:
        print(vetor[:: -1])    
    else:
        print('este código é inválido')
else:
    print(' Este código é inválido')