vetor = []
num = 0 
media = 0
cont = 1
while cont<= 5:
    num = input('digite um numero')
    if num.replace(".", "", 1).replace("-", "").isdigit():
       cont += 1
       vetor.append(float(num))

    else: 
        cont = cont
        print('digite um numero válido')

media = sum(vetor) / len(vetor)

print(f' o total de valores lidos é {vetor}\n O maior valor lido é {max(vetor)}\n O menor valor lido é {min(vetor)}\n A media dos valores é {media}')