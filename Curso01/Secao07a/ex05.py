vetor = []
num = 0
cont = 1
while cont <= 10:
    num = input('digite um numero')
    if num.isdigit():
        num = int(num)
        
        if num % 2 == 0:
            vetor.append(num)
        
        cont += 1
    else:
        cont = cont
        print('digite um numero válido')

print(f' ele possui {len(vetor) } numeros pares')