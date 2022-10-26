def volume_esfera(raio):
    pi = 3.1415
    volume = (4 * pi * raio ** 3)/3
    return volume


raio = input('digite o raio: ')
if raio.isdigit():
    raio = int(raio)
    print(f'o volume é {volume_esfera(raio)}')
else:
    print('digite um numero válido')

# teste com digite o raio: 5
# o volume é 523.5833333333334
# está rodando