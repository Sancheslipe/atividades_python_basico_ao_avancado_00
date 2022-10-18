vetor1 =[]
vetor2 = []
vetor3 = []
num = 0
cont = 0
while cont <= 19:
    num = input(' digite um numero ')
    if num.replace(".", "", 1).replace("-", "").isdigit():
        
        num = float(num)
        if cont >= 9:
            vetor2.append(num)
        else:
            vetor1.append(num)
        cont += 1
    else:
        cont= cont 
        print(' digite um numero válido')

for i,valor in enumerate(vetor1):
    if i % 2 == 0:
        print('pegou 1')
        vetor3.append(vetor1[i])
        print(vetor1[i])

for i,valor in enumerate(vetor2):
    if i %2 != 0:
        print('pegou 2')
        vetor3.append(vetor2[i])
        print(vetor2[i])

print(vetor3)