numerador = 1
soma = 0 
numerador = 1
denominador = 1
# while loopInfinito == True:
#     for a in range(1, 100, 2): 
#         print(a)
#         loopInfinito = False
#         for b in range(1,51 ):
#             print(f'passou por aqui')
#             print(b)
    

while (numerador >= 1) and (numerador <= 99) and (denominador >= 1) and (denominador <= 55):
    print('passou aqui')
    print(f'{numerador} / {denominador} = {numerador / denominador}') 

    soma = soma + (numerador / denominador) 
    numerador = numerador + 2 
    denominador = denominador + 1

print(f'O valor de S é {soma}')
