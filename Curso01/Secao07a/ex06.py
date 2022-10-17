vetor = []
cont = 1
num = 0

while cont <= 5:
    num = input('digite um numero')
    if num.replace(".", "", 1).isdigit():
        num = float(num)
        vetor.append(float(num))   
        cont += 1
    else:
        cont = cont
        print('digite um numero válido')

print(f'{max(vetor)} é o maior numero') #maximo valor
print(f'{min(vetor)} é o menor numero') #minimo valor