numero = input('digite um numero')
primeiroNum = 0
segundoNumImpar = 0
segundoNumPar = 0
segundoNum = 0
terceiroNum = 0
if numero.isnumeric():
    numero = int(numero)
else:
    print('digite um numero inteiro e positivo')

for n in range(1, numero +1 ):
    print(n)
    primeiroNum = primeiroNum + n 


for a in range(1, 2 * numero, ):
    if a % 2 == 0: 
        segundoNumPar = segundoNumPar + a
    else:
        segundoNumImpar = segundoNumImpar + a

segundoNum = segundoNumImpar - segundoNumPar

for b in range(1, 2 * numero, 2):
    terceiroNum = terceiroNum + b

print(f'O resultado da sequencia 1 é {primeiroNum}')
print(f'O rsultado da segunda sequência é {segundoNum}')
print(f'O resultado da terceira sequência é {terceiroNum}')
