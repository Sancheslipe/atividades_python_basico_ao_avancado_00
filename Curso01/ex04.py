def quadrado_perfeito(num):
    cont = 1 
    n1 = 1
    possui = 0

    while cont <= 100:
        
        n1 = cont
        resultado = n1 * n1
        
        if num == resultado:
            possui += 1
        
        cont +=1

    if possui >= 1:
        return print(' é um quadrado perfeito')
    else:
        return print(' não é um quadrado perfeito')


num = input('digite um numero: ')
if num.isdigit():
    num = int(num)
    quadrado_perfeito(num)
else:
    print('digite um numero válido ')

