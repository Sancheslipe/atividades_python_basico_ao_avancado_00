n = input('digite um numero inteiro e positivo')
valorE = 0

if n.isnumeric() == True and int(n) > 0:
    n = int(n)
else: 
    print('numero inválido')
valorE = 1

for num in range(1, n + 1):
    valorE = valorE + 1 / num
    print(valorE)

print(f' o valor E é {valorE}')