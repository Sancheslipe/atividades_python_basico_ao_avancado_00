# numero = float(input('Digite um número positivo: '))
# divisor = 2
# expoente = 1
# base = 0
# if numero > 0:

#     calculo = numero
#     while (calculo // divisor >= 
#     ):
#         print(f'{calculo} | {divisor}  ')
#         calculo = calculo / divisor
#         print(f'{calculo} ')
#         expoente = expoente + 1
#         divisor = + 1
#         print(f'o logaritmo é {expoente}')
        

numero = int(input('digite um numero'))
calcular = numero
base = 2 
expoente = 1
resultado = 2


if numero > 0:
    while (calcular % base ) != 0:
        base = base + 1
        resultado = base

    while (base < numero):
        base = base ** 2
        expoente = expoente + 1

        
print(f' a base é {resultado} o expoente é {expoente}')

