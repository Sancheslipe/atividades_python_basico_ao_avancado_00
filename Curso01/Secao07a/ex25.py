vetor = []
termina = False
executar = True
cont = 1
i = 1

while executar == True:
    if cont <= 100:
        # print(f' este é o i {i}')
        # print(f'este é o cont {cont}')
        
        if str(i)[-1:] == '7':
            termina = True
            # print("termina em 7--------------------------- {termina}", termina)
        else:
            termina = False
        
        if i % 7 == 0 or termina == True:
            vetor.append(i)
            # print(f'é divisivel por 7----------------\n\n\n')
            cont += 1
        else:
            cont = cont
        
        i += 1    
    else:
        executar = False
print(f'Este é o vetor {vetor}')
