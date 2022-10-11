# menorDivisivel = True
# divisor = 1
# numero = 1

# diviviuAnteriores = True
# #vai no for de 1 á 20
# menor = 0 #vai receber o menor numero divisivel


# while menorDivisivel == True:
    
#     for div in range(1, divisor +1):
#         print(numero)
#         if (numero % div == 0) :
#             menor = numero

#         else:
#             numero = numero + 1



# print(f' o menor numero divisivel de 1 - 5 é {numero}')

num = 1
div = 1
menorDivisivel = True

while menorDivisivel == True:
    if (num % div == 0 ):
        div = div + 1
    else:
        num = num + 1
        div = 1
    
    if div > 19:
        menorDivisivel = False

print(f'o numero final é {num}')