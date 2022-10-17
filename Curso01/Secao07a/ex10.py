vetor = []
nota= 0
cont  = 1
media = 0
while cont <= 15:
    nota  = input('digite a sua nota')
    if nota.replace(".", "", 1).isdigit() and (float(nota) >= 0 and float(nota) <= 10):
        vetor.append(float(nota))
        cont += 1

    else:
        cont = cont
        print('digite uma nota válida')

media = sum(vetor) / len(vetor)
print(f' a média geral é {media}')