"""
conjuntos 
- conjuntos em qualquer linguagem de programação,
    estamos fazendo referencia á teoria dos conjuntos em matemática
- aqui no python, os conjuntos são chamados de sets.
    dito isso na mesma for ma que na matemática:


- sets (conjuntos) Não possuem valores duplicados:
- sets (conjuntos) não possuem valores ordnados ;
- Elementos não são acssados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos,
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em python com chaves{}-

diferencça entre conjuntos (sets) e mapas (dicionários) em python:
    - um dicionário tem chaves /valor;
    - um conjunto tem apenas valor;

#definindo um conjunto:
#forma 1 

s =set({1,2,3,4,5,6,7,2,3}) #repare que temos valores repetidos.

print(s)
print(type(s))

#OBS: ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo 
# será ignorado sem gerar error e não fará parte do conjunto.

# forma 2

s = {1,2,3,4,5,5}
print(s)
print(type(s))

if 3 in s:
    print('tem o 3')
else:
    print(' não tem o 3 ')

#listas aceitam valores duplicados, então temos 10 elementos
lista = [ 99, 2, 34, 23, 12, 1, 44, 5, 34]
print(f' lista: {lista} com {len(lista)} elementos')
#tuplas aceitam valores duplicados, então temos 10 elementos
tupla =  99, 2, 34, 23, 12, 1, 44, 5, 34
print(f'tupla : {tupla}  com {len(tupla)} elementos')

#Dicionários não aceitam chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys([ 99, 2, 34, 23, 12, 1, 44, 5, 34], 'dict')
print(f'dicionário: {dicionario} com {len(dicionario)} elementos')
#Conjuntos não aceitam chaves duplicadas, então temos 8 elementos
conjunto = { 99, 2, 34, 23, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')


#podemos iterar com sets
for valor in s:
    pint(valor)
"""
#assim como todo outro conjunto em python podemos colocar tipos de dados misturados em sets]



