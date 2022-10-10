nota1 = float(input('digite a nota 1 '))
nota2 = float(input('digite a nota 2 '))
nota3 = float(input('digite a nota 3 '))

somaNota = (nota1 * 2 ) + (nota2 * 3 ) + (nota3 * 5)
mediapeso = 2 + 3 +5 
mediaNotas = somaNota / mediapeso

print(mediaNotas)

if mediaNotas >= 0 and mediaNotas <= 2.9:
    print(f'você esta reprovado {mediaNotas}')
elif mediaNotas >= 3 and mediaNotas <= 4.9:
    print(f'você está em recuperação {mediaNotas}')
else:
    # mediaNotas >=5.00:
    print(f'voce está aprovado')