numero = 1
menor = 0
menorDivisivel =True

while menorDivisivel == True:
    
    if (numero %1 == 0) and (numero % 2 == 0) and (numero %3 == 0) and (numero %4 == 0) and (numero %5 == 0) and (numero %6 == 0) and (numero % 7 == 0) and (numero %8 == 0) and (numero %9 == 0) and (numero %10 == 0) and (numero %11 == 0) and (numero % 12 == 0) and (numero %13 == 0) and (numero %14 == 0) and (numero %15 == 0) and (numero %16 == 0) and (numero % 17 == 0) and (numero %18 == 0) and (numero %19 == 0) and (numero %20 == 0):
        print('a lógica tá certa!')
        menor = numero
        menorDivisivel = False
 
    numero = numero + 1
         

print(f'o menor numero divisivel é {menor}')
