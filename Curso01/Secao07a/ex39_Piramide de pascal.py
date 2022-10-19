"""
UTILIZANDO A TÉCNICA DO GRINGO

se o código te fez passar raiva, comenta ele todo por que daí o conhecimento já fixa na mente!

"""
vetor = []
n = 0
cont = 0 

#diz o tamanho do triangulo de pascal
n = input('digite um numero referente ao numero de linhas que deseja ver')
#verifica se é um numero inteiro
if n.isdigit():
    n = int(n) -1 # o menos 1 é pra dar o numero de linhas certinho

#   enquanto o contador (que começa em 0) for menor ou igual o numero digitado 
#   [para fazer em for é só tirar o contado e colocar for cont in range(0, n +1)]

    while cont <= n:

        #identação necessária para o vetor apender adicionar o cont e printar o vetor
        # e tratativa para ver se tem numero igual a zero(não printa nada) ou negativo
        if cont >= 0:
            #for para indicar o index para o vetor.appender()

            for a in range(len(vetor) - 1):

                #vetor apendendo a linha referente no index que juntando tudo dá  a piramide

                vetor.append(vetor[a] + vetor[a +1])

            #este daqui é só para cortar os numeros excedentes

            for b in range(len(vetor) - cont):    
                vetor.pop(1)
                # vetor.append(1)
                # esse de cima era pra tentar apender no final, mas deu ruim e 
                # só está aqui para mim lembrar de não tentar adicionar denovo (como tentei um monte de vezes)
        
        
        #digitou negativo cai aqui
        else:
            print('Digite um numero positivo')

        vetor.append(1)        
        cont += 1
        print(vetor)    


#caso não é um digito vai printar isso
else:
    print('digite um numero válido')
