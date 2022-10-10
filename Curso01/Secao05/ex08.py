nota1 = float(input(' digite a primeira nota '))
nota2 = float(input('digite a segunda nota'))

# validação de nota valida 1 

if nota1 <= 10.00 and nota1 >= 0.00:
    somaNota = nota1
elif nota1  > 10.01 or nota1 < -0.01:
    print(f' a nota 1 é inválida ')


# validação de nota valida 2 

if nota2 <= 10.00 and nota2 >= 0.00 :
    somaNota = nota1 + nota2
    print(f' a média das notas é {somaNota / 2 }')
elif nota2  > 10.01 or nota2 <- 0.01:
    print(f'  nota 2 é inválida')


