vetor = []
num = 0
cont = 1
while cont <= 10:
    num = input('digite um numero')
    if num.replace('.', '', 1).replace('-', '').isdigit():
        num = float(num)
        if num in vetor:
            cont = cont
            print('digite outro numero, este já foi')
        else:
            cont += 1
            vetor.append(num)
    else:
        cont = cont
        print('digite um numero válido')

print(f'os numeros lidos são estes {vetor}')