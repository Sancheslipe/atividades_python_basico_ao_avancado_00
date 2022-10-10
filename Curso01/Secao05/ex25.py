valorA = float(input('digite o valor de A'))
valorB = float(input('digite o valor de B'))
valorC = float(input('digite o valor de C'))

delta = valorB ** 2  - (4 * (valorA * valorC))


x1 = ((-valorB) + ((delta) ** 0.5)) / (2 * valorA)

x2 = ((-valorB) - ((delta) ** 0.5)) / (2 * valorA)

if delta < 0 :
    print('Não exite raiz')

if delta == 0:
    print(f'é valorA unica raiz possivel{(x1) ** 0.5}')

if delta >= 0:
    print(f'{x1} , {x2} são os resultados das raizes')

