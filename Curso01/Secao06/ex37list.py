numeros = []
dividir = ''
soma = 0 
quadrado = 0

for i in range(1000, 9999 + 1):
    dividir = str(i)
    soma = int(dividir[0:2]) + int(dividir[2:5])
    quadrado = soma ** 2
    if quadrado == i:
        numeros.append(str(i))


print(f'os numeros come ssa propriedade são {numeros}')

