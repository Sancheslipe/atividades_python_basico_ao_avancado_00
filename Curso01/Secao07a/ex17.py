vetor  = []
num = 0
cont = 1

while cont <= 5:
    num = input('digite um numero') 
    if num.replace(".", "", 1).replace("-", "").isdigit():
        cont += 1
        num = float(num)
        if num >0:
            vetor.append(num)
        else:
            vetor.append(0)
    else:
        cont = cont
        print('digite um numero válido')

print(vetor)