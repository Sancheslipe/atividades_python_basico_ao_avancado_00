vetor1 = []
vetor2 = []
indexMaior = 0
maior = 0
indexMenor = 0
menor = 99999999999

numero = 0
altura = 0.0
cont = 0

while cont <= 9:
    numero = input('digite o numero do aluno')
    if numero.isdigit():
        numero = int(numero)
        altura = input('digite a altura do aluno')
        if altura.replace(".", "", 1).isdigit():
            altura = float(altura)
            
            
            vetor1.append(numero)     
            vetor2.append(altura)
            cont +=1
        else:
            cont = cont
            print('digite uma altura válida')   
    else:
        cont = cont
        print('digite um numero válido')

maior = max(vetor2)
menor = min(vetor2)
 
indexMaior = vetor2.index(maior)

indexMenor = vetor2.index(menor)


print(f' a maior altura é {maior}, pertence ao aluno {vetor1[indexMaior]}\n A menor altura é {menor}, pertence ao aluno{vetor1[indexMenor]}')