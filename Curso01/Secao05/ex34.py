nota = float(input('digite as notas do aluno'))
faltas = int(input('digite a quantidade de faltas'))
conceito = 1
letraConceito = ''

"""
5 = a
4 = b
3 = c
2 = d
1 = e
"""

if nota >= 9 and nota   <= 10  and faltas <  20:
    conceito = 5 


elif nota >= 9 and nota <= 10    and faltas >= 20:
    conceito = 4


elif nota >= 7.5 and nota <= 8.9 and faltas < 20:
    conceito = 4 


elif nota >= 7.5 and nota <= 8.9 and faltas >= 20:
    conceito = 3 

elif nota >= 5.0 and nota <= 7.4 and faltas < 20:
    conceito = 3
   

elif nota >= 5.0 and nota <= 7.4 and faltas >= 20:
    conceito = 2 

    
elif nota >= 4.0 and nota <= 4.9 and faltas < 20:
    conceito = 2


elif nota >= 4.0 and nota <= 4.9 and faltas >= 20:
    conceito = 1


elif nota>= 0.0 and nota <= 3.9 and faltas < 20:
    conceito = 1 


elif nota>= 0.0 and nota <= 3.9 and faltas >= 20:
    conceito = 1 


if conceito == 5:
    print(5)
    letraConceito ='A'
elif conceito == 4:
    print(4)
    letraConceito ='B'
elif conceito == 3:
    print(3)
    letraConceito ='C'
elif conceito == 2:
    print(2)
    letraConceito ='D'
elif conceito == 1:
    print(1)
    letraConceito ='E'


print(f'Este é o seu conceito {letraConceito}')