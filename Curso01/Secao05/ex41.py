peso = float(input(' digite o seu peso em kilos'))
altura = float(input(' digite a sua altura em metros'))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(' Abaixo do Peso')
elif imc >= 18.6 and imc <= 24.9 :
    print(' Saudável')
elif imc >= 25.0 and imc <= 29.9 :
    print(' Peso em excesso')
elif imc >= 30.0 and imc <= 34.9 :
 
    print(' obesidade Grau |')
elif imc >= 35.0 and imc <= 39.9 :
    print(' obesidade Grau ||(severa)')
elif imc >= 40.0 :
    print(' obesidade Grau ||| (mórbida)')