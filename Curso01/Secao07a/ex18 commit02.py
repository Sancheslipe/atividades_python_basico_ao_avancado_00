vetor = []
num = 0 
multiplo = 0
cont = 1
cont2 = 1
index = 0
multiplos = []

while cont <= 10:
    num = input('digite um numero')
    if num.replace(".", "", 1).replace("-", "").isdigit():
        cont += 1
        num = float(num)
        vetor.append(num)
    else:
        cont = cont
        print('digite um numero válido')

multiplo = input('digite um numero inteiro')

while cont2 < 2:
    if str(multiplo).isdigit():
        cont2 += 1
        multiplo = int(multiplo)
    else:
        cont2 = cont2
        print('digite um numero inteiro válido')

while index <=9:
    if vetor[index] % multiplo == 0:
        multiplos.append(vetor[index]) 

    index += 1

print(f' os numeros lidos que são multiplos de {multiplo} são {multiplos} ')

