vetor1 = []
vetor2 = []
num = 0
cont = 0 
produtoEscalar = 0

while cont <= 9:
    num = input('digite um numero ')
    if num.replace(".","", 1).replace("-", "").isdigit():
        num = float(num)

        if cont <=4:
            vetor1.append(num)
        else:
            vetor2.append(num)
        
        
        
        cont += 1  
    else:
        cont = cont
        print('digite um numero válido')

for i in range(0,4 +1):
    produtoEscalar += (vetor1[i] * vetor2[i])

print(f' o produto escalar é {produtoEscalar}\n Vetor1 {vetor1}\n Vetor2 {vetor2}')  