vetor = []
num = 0
cont = 1

while cont <= 6:
    num = input('digite um numero inteiro e par')
    if num.isdigit() and int(num) % 2 == 0 :
        vetor.append(int(num))
        cont += 1
    else:
        cont = cont
        print('digite um numero inteiro e par')
print(vetor[::-1])