matriz = [[],[],[],[],[]]
transposta = [[],[],[],[],[]]
coluna = []
matricula = 0
mediaProva = 0
mediaTrabalho = 0
soma = 0
notaFinal = 0
maior = 0
somaGeral = 0
media = 0
escolha = ''

for l in range(0,5):
    for c in range(0,4):
        
        if c == 0:
            matricula = int(input('digite a sua matricula  '))
            coluna.append(matricula)
            matriz[l].append(coluna[:])
            coluna.clear()
        
        if c == 1:
            mediaProva = int(input('digite a media das notas da sua prova  '))
            soma = mediaProva
            coluna.append(mediaProva)
            matriz[l].append(coluna[:])
            coluna.clear()
        
        if c == 2:
            mediaTrabalho = int(input('digite a media dos trabalhos  '))
            soma += mediaTrabalho
            coluna.append(mediaTrabalho)
            matriz[l].append(coluna[:])
            coluna.clear()
        
        if c == 3:
            notaFinal = soma
            somaGeral += notaFinal
            coluna.append(notaFinal)
            matriz[l].append(coluna[:])
            coluna.clear()
            if notaFinal > maior:
                maior = matricula
        
    soma = 0

for l in range(0,5):
    for c in range(0,4):
        transposta[c].append(matriz[l][c])


escolha = input('se voce deseja ver em Matriz digite [M], se voce deseja ver em transposta digite [t]')
if escolha.upper() == 'M':

        
    print(f'matricula,', end='')

       
    print(f'prova,', end='')
        
        
    print(f'trabalho,', end='')
        
        
    print(f'nota final')

    for l in range(0,5):
        
        for c in range(0,4):
            print(f'{matriz[l][c]:}', end = ' ')
        print()
    media = somaGeral /4

    print(f'\nA matricula do aluno com a maior nota final é {maior}')
    print(f' a média das notas finais é {media}')
else:
    for l in range(0,4):
        if l == 0:
            print(f'matricula', end='  :')

        if l == 1:
            print(f'prova', end='      :')
        
        if l ==2:
            print(f'trabalho', end='   :')
        
        if l == 3:
            print(f'nota final', end=' :')

        for c in range(0,5):
            print(f'{transposta[l][c]:}', end = ' ')
        print()

media = somaGeral /5

print(f'\nA matricula do aluno com a maior nota final é {maior}')
print(f' a média das notas finais é {media}')




