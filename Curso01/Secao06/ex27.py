num = input('digite um numero')

infinito = float('inf')
numHarmonico = 1

if num.isnumeric() == True:
    num = int(num)
else:
    print('digite um numero inteiro')

for n in range(1, num +1):
    print(f'{numHarmonico} + {1/n}')

    numHarmonico = numHarmonico + 1 / n

print(numHarmonico)