import random
numAleatorio = (random.randint(1, 1000))
chute = 0
executar = True
tentativas = 0

while executar == True:
    chute = input('digite um numero')
    if chute.isdigit():
        chute = int(chute)
        tentativas = tentativas + 1

        if chute == numAleatorio:
            print('parabéns você acertou')
            executar = False
        elif chute > numAleatorio:
            print('seu chute foi maior que o numero gerado')
        elif chute < numAleatorio:
            print('seu chute foi menor que o numero gerado')    
    else:
        executar = False
        print(f'digite um numero válido')

print(f' o total de tentativas foi {tentativas}')