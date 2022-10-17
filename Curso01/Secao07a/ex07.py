vetor = []
num = 0 
cont = 1
maior = 0
while cont <= 10:
    num = input('digite um numero')
    if num.isdigit():
        vetor.append(int(num))
        cont += 1


    else:
        cont = cont
        print('digite um numero inteiro válido')

maior = max(vetor)
print(f'o maior elemento é {max(vetor)}, e a posição que ele se encontra é a posição dele é {vetor.index(maior)}')

