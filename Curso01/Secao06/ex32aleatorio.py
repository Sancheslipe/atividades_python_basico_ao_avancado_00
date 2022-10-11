import random


n = input('digite o numero de vezes que foram lançados os dados')
vezes = 1
if n.isdigit() and int(n) > 0:
    n = int(n)
else:
    print('digite um numero válido')

while vezes <= n:
    d1 = (random.randint(1, 6))
    d2 = (random.randint(1, 6))
    if d1 > d2:
        print(f'{d1}>{d2}')
    elif d2 >d1:
        print(f'{d2}>{d1}')
    elif d1 == d2:
        print(f' O Valor dos dados é semelhante\n{d1} = {d2}')
