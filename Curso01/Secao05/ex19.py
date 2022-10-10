num = int(1)

divisivel = ''

while(num < 10):
    if (num %3 == 0) or (num % 5 == 0 ):
        divisivel = str(num) + ', '
    num = num + 1
    print(f'{divisivel} é um numero divisivel por 3 ou 5 ')

 
