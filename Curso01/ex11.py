def media(nota1,nota2,nota3, letra):
    soma  = float(nota1) + float(nota2) + float(nota3)
    peso  = 5+ 3+ 2
    if str(letra).upper() == 'P':
        mediaP = soma / peso
        return mediaP
    elif str(letra).upper() == 'A':
        mediaA = soma / 3
        return mediaA


nota1 = input('digite a nota1: ')
if nota1.replace('.','', 1).replace('-','').isdigit():
    nota1 = float(nota1)
    nota2 = input('digite a nota2: ')
    if nota2.replace('.','', 1).replace('-','').isdigit():
        nota2 = float(nota2)
        nota3 = input('digite a nota3: ')
        if nota3.replace('.','', 1).replace('-','').isdigit():
            nota3 = float(nota3)
            letra = input('digite [P] para media Ponderada ou [A] para média Aritmética')
            
            if letra.upper() == 'P' or letra.upper() == 'A':
                print(media(nota1,nota2,nota3,letra))

            else:
                print('digite uma letra válida')



        else:
            print('digite uma nota válida')

    else:
        print('digite uma nota válida')

else:
    print('digite uma nota válida')
