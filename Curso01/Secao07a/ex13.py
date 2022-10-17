vetor = []
num = 0
cont = 1
menor = 0 
maior = 0

while cont <= 5:
    num = input(' digite um valor')
    if num.replace(".", "", 1).replace("-", "").isdigit():
        cont += 1
        vetor.append(float(num))

    else:
        cont = cont
        print(' digite um valor válido')

menor = min(vetor)
maior = max(vetor)
print(f' A posicção onde se eoncontra o maior numero lido é {vetor.index(maior)}\n A posição onde se encontra o menor numero lido é {vetor.index(menor)}')