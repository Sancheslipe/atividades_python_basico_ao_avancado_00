# VALIDAÇÃO PARA SABER SE O USUÁRIO UTILIZOU FLOAT OU QULQUER OUTRA COISA
num1 = input('digite um numero')


if num1.replace(".", "", 1).isdigit():
    num1 = float(num1)
    print(num1)
else:
    print('não rodou')
