print('digite o simbolo referente à qual você prefere\n')
operacao = input(' [1] Soma de 2 numeros,\n [2] diferença de 2 numeros (maior pelo menor),\n [3] produto entre 2 numeros,\n [4] divisão entre 2 numeros ( o dominador não pode ser 0\n Opção:')

num1 = float(input('digite o primeiro numero'))
num2 = float(input('digite o segundo numero'))
resultado = 0

if operacao == '1':
    resultado = num1 + num2
    print(f' o resultado é {resultado}')

elif operacao == '2':
    if num1 > num2:
        resultado = num1 - num2
    elif num1 < num2:
        resultado = num2 - num1
    print(f' o resultado é {resultado}')    
elif operacao == '3':
    resultado = num1 * num2
    print(f' o resultado é {resultado}')
elif operacao == '4':
    if num2 > 0 :
        resultado = num1 / num2
        print(f' o resultado é {resultado}')
    else:
        print('o numero 2 (denominador) não pode ser igual a zero!\n Tente Novamente')
else:
    print(f'você digitou uma operação inválida')