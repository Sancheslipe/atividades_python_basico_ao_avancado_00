vetorDesord = []
vetorOrd= []
aList = []
bList = []
a = 0
b = 0
stringA = ''
stringB =''
cont = 1
soma = 0


while cont <=1:
    a = input('digite o primeiro Numero')
    if (a.replace('.','', 1).isdigit()) and (float(a) < 10000):
        a = a
        vetorDesord.append(float(a))
        aList.append(list(a))
        aList[0].sort()
        
        stringA = ''.join(aList[0])
        
        vetorOrd.append(stringA)
        
        print(f' este é o aList {aList}')
        print(f' este é o vetor {vetorOrd}')

        b = input('digite o Segundo Numero')
        if (b.replace('.','', 1).isdigit() and (float(b) < 10000)):
            b = b
            vetorDesord.append(float(b))
            bList.append(list(b))
            bList[0].sort()
            stringB = ''.join(bList[0])
            vetorOrd.append(stringB)
            


            cont += 1
        else:
            cont = cont
    
    else:
        cont = cont
        print('Digite um numero válido')

soma = vetorDesord[0] + vetorDesord[1]

print(f'os numeros orde nados ficam {list(vetorOrd[0]) + list(vetorOrd[1])}, e a soma é {soma} ')



# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
# curso = ' '.join(lista6)
# print(curso)

#transforma uma palavra em letrinhas menores
# curso = ['palavra01', "palavra02"]

# print(list(curso[0])[1])