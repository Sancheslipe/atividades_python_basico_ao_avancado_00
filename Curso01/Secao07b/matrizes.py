"""
ANOTAÇÕES DO YOUTUBE

MATRIZES SÃO APENAS ARRAYS COM ARRAYS, LISTAS COM LISTAS

MATRIZ 4 X 4 == LISTA COM 4 LISTAS CONTENDO 4 COLUNAS
MATRIZ 3 X 10 == LISTA COM 10 LISTA CONTENDO 3 COLUNAS

PARA DECLARAR UMA MATRIZ TEM VARIOS JEITOS 1 DELE É


matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = 0
maior = 0
somaColuna = 0
for linha in range(0,3): # para 'linha' num range do tamanho de 0 até o indice de cada coluna.
    for coluna in range(0,3): #para 'coluna' num range do tamanho de 0 até o indice de cada coluna
        matriz[linha][coluna] = int(input(f'digite um valor'))
    
print('-=' *30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]

    print()


for linha in (range(0,3)):
    somaColuna += matriz[linha][2]
print(f' a soma dos valors pars é {pares}')
print(f' a soma dos valores da terceira coluna é {somaColuna}')

for coluna in range(0,3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]

print(f' o maior da terceira coluna é {maior}')
"""

''',
ARRAYS, UNIDIMENSIONAL, E MULTIDIMENSIONAL.

PARA GERAR UMA LISTA 3X3 É UTILIZADO DESTA MANEIRA

num = 1
for lista in range(1,4):
    for coluna in range(1,4):
        print(coluna)

print(lista)

'''
#fórmula base para uma matriz 1x3


# matriz = list()
# dado = list()
# num = 0
# nome = ''
# cont = 0
# while cont <= 2:
#     nome = input('digite seu nome \n')
#     num = input('digite um numero \n')
    
#     if num.isdigit():
#         print(cont)
#         num = int(num)
#         dado.append(f' nome: {nome}')
#         dado.append(num)
#         matriz.append(dado[:])
#         dado.clear()
#         cont+= 1


#     else:
#         cont = cont
#         print('digite um numero válido')

# for i in range(0,3):
#     print(f'[{matriz[i]}]')
#_____________________________________-----------------______________________------------------------_____________----------
# matriz = list()
# coluna = list()
# num = 0
# nome = ''
# cont1 = 0
# cont2 = 0

# while cont1<=2:
#     print(f' este é o cont1 {cont1}')

#     while cont2 <=1:
#         print(f' este é o cont2 {cont2}')
        
#         # nome = input(' digite seu nome\n')
#         num = input('digite um numero\n')
        
#         if num.replace('.','', 1).replace('-','').isdigit():
#             num = float(num)
            
#             # coluna.append(f'nome : {nome}')
#             coluna.append(f'idade :{num}')
#             matriz.append(coluna[:])
#             coluna.clear()
#             cont2 += 1
          
#         else:
#             cont2 = cont2
#             print('digite um numero válido')
    
#     cont1 += 1
#     cont2 = 0


# print('-=' * 35)

# for l in range(0,4):
#     for c in range(0,1):
#         print(f'linha {l}, coluna {c},')
#         print()
#         print(f'[{matriz[l][c]}]', end= '')
#         print()

# linho =  [[]]*3 #forma1 
# print(linho)    


linha = [[],[],[],[]]#4 arrays com posições cada [[]]*3
# linho = ,
coluna = []

# linho = 
# print(linho)
# coluno = []

for l in range(0,4):
    for c in range(0,4):
        coluna.append(int(input('Idade:  ')))
        linha[c].append(coluna.copy())
        coluna.clear()


for l in range(0,3):
    for c in range(0,3):
        print(linha[c][l], end=' ')
    print()