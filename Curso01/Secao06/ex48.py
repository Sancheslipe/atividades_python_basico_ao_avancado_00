fibonacci = []

antecessor = 0
sucessor  = 1
executar = True

while executar == True:
    fibonacci.append(str(antecessor))
    fibonacci.append(str(sucessor))
    antecessor = antecessor + sucessor 
    sucessor = sucessor + antecessor
    
    if sucessor > 4000000: #4 000 000
        executar =False
    

print(fibonacci)

