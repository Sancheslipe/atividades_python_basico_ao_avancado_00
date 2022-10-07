num = 0 
maior = 0
menor = 99999999999

for i in range(1,11):
    num = int(input(' Digite um numero'))
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

print(f'o maior numero é {maior} e o menor numero é {menor}')
