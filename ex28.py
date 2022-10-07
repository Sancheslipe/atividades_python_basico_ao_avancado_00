x = int(input('digite o primeiro X'))
y = int(input('digite o primeiro Y'))
z = int(input('digite o primeiro Z'))

operacao = input(('Digite a media que deseja que seja efetuada\n(a) Geométrica:\n(b) Ponderada:\n(c) Harmônica:\n(d) Aritmética:'))


if operacao == 'a':
    media = (x * y * z) ** (1/3) 
elif operacao == 'b':
    media = (x + (2 * y) + (3 * z)) / 6
elif operacao == 'c':
    media = 1 / ((1/x) + (1/y) + (1/z))  
elif operacao == 'd':
    media = (x + y + z) / 3

print(f' a média deu um total de {media}')

