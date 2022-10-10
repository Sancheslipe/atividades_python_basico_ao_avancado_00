multiplos = []
soma = 0
num = input('digite um numero')

if num.isdigit() == True:
    num = int(num)
else:
    print('dogote um numero válido!')

for num in range(num, num +20):
    if num % 11 == 0 or num % 13 == 0 or num % 17 ==0:
        multiplos.append(str(num))
    
print(f'O primeiros multiplo dos numeros 11, 13 e 17 após o numero digitado é \n{multiplos[0]}')