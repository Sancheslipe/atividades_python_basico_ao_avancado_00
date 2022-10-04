nome1 = input('Digite seu nome ')
valorInvestido1 = int(input(f'{nome1} digite quanto você investiu! '))

nome2 = input('Digite seu nome ')
valorInvestido2 = int(input(f'{nome2} digite quanto você investiu! '))

nome3 = input('Digite seu nome ')
valorInvestido3 = int(input(f'{nome3} digite quanto você investiu! '))

premio = int(input('Digite o valor do premio '))

valorGeral = valorInvestido1 + valorInvestido2 + valorInvestido3

valor1 = valorInvestido1 * 100 
premio1 = ((valor1 / valorGeral) * premio) / 100

valor2 = valorInvestido2 * 100 
premio2 = ((valor2 / valorGeral) *  premio) / 100

valor3 = valorInvestido3 * 100 
premio3 = ((valor3 / valorGeral) *  premio) / 100

print(f'{valor1} {valor2} {valor3} {valorGeral} ')
print(f'{premio1} {premio2} {premio3} {premio} ')

print(f' O (a) ganhador {nome1} Ganharia {round(premio1,2)},')
print(f' O (a) ganhador {nome2} Ganharia {round(premio2,2)} e  ')
print(f' O (a) ganhador {nome3} Ganharia {round(premio3,2) } ')

# valorGeral -   100
#  valor1         x