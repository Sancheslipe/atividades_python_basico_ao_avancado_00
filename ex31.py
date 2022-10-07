altura = float(input('digite a sua altura'))
peso = float(input('digite o seu peso'))

if altura < 1.20 :
    if peso <= 60:
        print(f'você está na categoria A')
    elif peso > 60 and peso <= 90:
        print(f'Você está na categoria D')
    elif peso >90:
        print(f' Você está na categoria G')
elif altura >= 1.20 and altura <= 1.70 :
    if peso <= 60:
        print(f'você está na categoria B')
    elif peso > 60 and peso <= 90:
        print(f'Você está na categoria E')
    elif peso >90:
        print(f' Você está na categoria H')
elif altura > 1.70 :
    if peso <= 60:
        print(f'você está na categoria C')
    elif peso > 60 and peso <= 90:
        print(f'Você está na categoria F')
    elif peso >90:
        print(f' Você está na categoria I')