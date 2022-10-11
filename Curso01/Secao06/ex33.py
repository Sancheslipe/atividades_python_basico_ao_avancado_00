n = input(' digite um numero')
multiplos = 1
listMultiplos = []
num = 1
if n.isnumeric():
    n = int(n)
else:
    print('digite um numero positivo')

i = input('digite um numero inteiro positivo e diferente de zero')

if (i.isnumeric()) and (int(i) > 0) and (int(i) != 0):
    i = int(i)
else:
    print('digite um numero inteiro positivo diferente de zero')

j = input('digite um numero inteiro positivo e diferente de zero')

if (j.isnumeric()) and (int(j) > 0 ) and (int(j) != 0 ):
    j = int(j)
else:
    print('digite um numero inteiro positivo diferente de zero')

#fazendo a tratativa dos dados recebidos pelo usuário!

while multiplos <=5:   
    for num in range(0, n + 3):
        if (num % i == 0 and num % j == 0 ) or (num % j == 0) or (num % i == 0) :
            listMultiplos.append(str(num))
            multiplos = multiplos + 1

print(f' a lista é {listMultiplos[0:6]}')