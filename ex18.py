N = int(input('digite quantas vezes devemos repetir'))
numero = 0
maior = 0
vezes = 0 

for N in range(0, N):
    numero = int(input('digite um numero'))
    if numero > maior:
        maior = numero
        if numero == maior:
            vezes = vezes + 1

print(f'o maior numero é {maior}, e o numero de vezes que o maior numero foi lido foram {vezes}')