nota1 = float(input('digite a nota 1 '))
nota2 = float(input('digite a nota 2 '))
nota3 = float(input('digite a nota 3 '))

somaNota = (nota1 * 1 ) + (nota2 * 1 ) + (nota3 * 2)
mediapeso = 1 + 1 +2 
mediaNotas = somaNota / mediapeso

print(somaNota)

if somaNota >= 60:
    print(f'você foi aprovado {somaNota}')
else:
    print(f'você foi reprovado {somaNota}')