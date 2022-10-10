multiplos = []
soma = 0
num = 0

for num in range(1, 1000):
    if num % 3 == 0 or num % 5 == 0:
        multiplos.append(str(num))

for index, mult in enumerate(multiplos):
    soma = soma + int(multiplos[index])

print(f' a soma é {soma}')