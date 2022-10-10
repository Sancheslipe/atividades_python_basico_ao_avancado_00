print('digite o simbolo referente à qual você prefere\n')
operacao = input(' [-] subtração,\n [+] adição,\n [*] multiplicação,\n [/] divisão')  
num1 = int(input('digite o primeiro numero'))
num2 = int(input('digite o segundo numero'))
resultado = 0

if operacao == '-':
    resultado = num1 - num2
    print(f' o resultado é {resultado}')
elif operacao == '+':
    resultado = num1 + num2
    print(f' o resultado é {resultado}')
elif operacao == '*':
    resultado = num1 * num2
    print(f' o resultado é {resultado}')
elif operacao == '/':
    resultado = num1 / num2
    print(f' o resultado é {resultado}')
