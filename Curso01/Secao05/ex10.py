altura = float(input('digite a sua altura '))
sexo = input('digite o seu sexo [F] para feminino e [M] para masculino ')

if sexo.upper() == 'M':
    print(F'o seu peso ideal é {(72.7 * altura) - 58}')
if sexo.upper() == 'F':
    print(F'o seu peso ideal é {(62.1 * altura) - 44.7}')