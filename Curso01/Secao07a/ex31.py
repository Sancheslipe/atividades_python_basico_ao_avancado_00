vetor = []
vetor2 = []

num = 0
cont  = 1
while cont <= 20:
    num = input('digite os numeros da primeira lista !NÃO PODE HAVER VALORES REPETIDOS!')
    
    if num.replace('.','', 1).replace('-','').isdigit():
        num = float(num)
        cont += 1
        if cont<=10:
            vetor.append(num)
            
        else:
            vetor2.append(num)
    else:
        cont = cont 
        print('digite um numero válido')

uniao = set(vetor).union(vetor2)
print(f' A uniao entre os dois é {uniao}')
