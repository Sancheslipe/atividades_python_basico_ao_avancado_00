num = input('digite um numero')
cont = 1
divisores =  []
soma = 0 
if num.isdigit() == True:
    num = int(num)

else:
    print('digite um numero')


while cont <= num:
    if num % cont == 0:
        divisores.append(str(cont))
    cont += 1

for index , div in enumerate(divisores):
    print(divisores[index])
    soma = soma + int(divisores[index])
    
soma = soma - num
# print(f'Estes são os divisores {divisores} ')

print(f'esta é a soma {soma} ')