def voluma_cilindro(raio, altura):
    pi = 3.141592
    result = pi * (raio ** 2) * altura
    return result


raio = input('digite o raio: ')
if raio.replace('.','', 1).isdigit():
    raio = float(raio)
    altura  = input(' digite a altura: ')
    if altura.replace('.','', 1).isdigit():
        altura = float(altura)

        print(f'o volume do cilindro é {voluma_cilindro(raio,altura)}')

    
    else:
        print('digite um numero válido')





else:
    print('digite uma altura valida')
