matriz = []
coluna = []
matricula = []
media = []
soma = 0
resposta = 0
line = 0
col = 0

while line <3:
    matricula.append(input('Digite sua matricula abaixo!\n'))
    while col <10:
        resposta = input('digite a sua nota')
        if resposta.replace('.','', 1).isdigit():
            col += 1
            coluna.append(float(resposta))
            soma += float(resposta)
        else:
            col = col
            print(' digite um numero válido')

    matriz.append(resposta[:])
    media.append(soma / 10)
    soma = 0
    coluna .clear()

    line += 1
    col = 0

for l in range(0,3):
    print(f'\naluno de matricula: {matricula[l]}\n')
    print(f'Notas',end=':')
    for c in range(0,10):
        print(matriz[l], end=' ')
    print()
    if media[l] >= 7.00:
        print(f' Aprovado, a media é: {media[l]}')
    else:
        print(f' Reprovado, a média é: {media[l]}')
