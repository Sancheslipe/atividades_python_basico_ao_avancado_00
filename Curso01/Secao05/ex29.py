import random
num1 = 1
numeroQuestao1 = 1
num2 = 1
questoes = 1 
numeroQuestao2 = 2
pontos = 0


while(questoes < 6):
    
    numeroQuestao1 = (random.randint(1, 100))

    numeroQuestao2 = (random.randint(1, 100))  

    print(f' Qual o resultado da operação {numeroQuestao1} + {numeroQuestao2} ??')
    resposta = int(input(' Digite a resposta '))
    respostaCerta = numeroQuestao1 + numeroQuestao2 

    if  resposta != respostaCerta:
        print(f'você errou a resposta certa é {respostaCerta} ')

    else:
        print(f'Você acertou, a resposta certa é {respostaCerta}')
        pontos = pontos + 1

    questoes = questoes +  1

print(f'a sua pontuação foi de {pontos} pontos!')


