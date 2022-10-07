num = int(input('digite um numero'))
contador = 0
somaAlgarismo = 0 

if num > 0 :
    algarismo = int(input('digite a quantidade de algarismos deste numero'))
    algarismo = algarismo - 1 
    

    while (contador <= algarismo):
        somaAlgarismo = somaAlgarismo + int(str(num)[contador])
        contador += 1

    print(somaAlgarismo)
else:
    print('Número inválido')

    
    # ajuda do henrique
    # for index in range (len(str(num))):
    #     print(index)
    #     print(str(num)[index])

"""

Anotações

Anotações

num = numero informado
algarismos = 2
somaAlgarismo
contador

enquanto algarismo for menor que 2 
calculo = calculo + algarismo de index referente ao contador []
---------------------------------------------------------------------
caso 
num = 15 (numero informado pelo sistema)
algarismo = 2 (numero informado pelo sistema)

código

contador = 0
somaAlgarismo = 0 
numero == 15

if num > 0 :
	algarismo ==2

	algarismo = 2 - 1 

		enquanto contador for menor ou igual ao algarismo
			somaAlgarismo = somaAgarismo + algarismo[contador]
			contador ++
else:
print(f'Número inválido')


"""