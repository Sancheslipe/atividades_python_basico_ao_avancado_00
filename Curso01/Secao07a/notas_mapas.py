"""
conhecidos em python como dicionários 

dicionários em python são representados {chves}



receita = {'jan' : 100, 'fev' : 250, 'mar' : 400} 
print(receita)



#iterar sobre dicionários 

for chave in receita:
    print(chave)

for chave in receita:
    print(f'em {chave} recebi R$ {receita[chave]}')

#acessano as chaves

for chave in receita.keys():
    print(receita[chave])

# acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)

#desempacotamento de dicionários

for chave, valor in receita.items():
    print(f'chave = {chave} e valor {valor}')


print(receita.keys())


# soma , valor máximo, valor minimo, tamanho 
# se os numeros forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))
"""