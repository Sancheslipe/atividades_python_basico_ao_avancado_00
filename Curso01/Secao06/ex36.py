somaQuadrada = 0
somaComun = 0
quadrado = 0
resultadoFinal = 0
for i in range(1, 101):
    somaQuadrada = somaQuadrada + (i **2)

for a in range(1,101):
    somaComun = somaComun + a

quadrado = somaComun **2

resultadoFinal = quadrado - somaQuadrada
print(f'o resultado final de {quadrado} - {somaQuadrada} = {resultadoFinal}')