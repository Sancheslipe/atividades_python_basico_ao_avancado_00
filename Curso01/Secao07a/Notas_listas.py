"""
listas

listas em pthon funciona como vetores/Matrizes (arrays) em outras linguagens, com a diferença de serem DINÂMICO e
 também de podermos colocar Qualquer tipo de dados.

Em python :

- dinâmico: não possuem tamanho fixo ou seja, podemos criar a Lista e simplesmente ir adicionando elementos:
- qualquer tipo de dado: não possuem dados fixos; ou seja podemos colocar qualquer tipo de dados.

Em python listas são representadas por colchetes ex: list = [] # estou inicializando uma lista vazia chamada list:

# para achar algum item em uma lista
# if 8 in lista3:
#     print('achei')
# else:
#     print('não achei')

# print(lista1)
# lista1.sort()
# print(lista1)

#para adicionar elementos ou valores em um lista utilizamos a função append()
#com append só conseguuimos adicionar um elemento por vez, mas é possivel adicionart uma lista dentro de outra lista
lista1.append(42) 1 só

#coloca uma lista como elemento unico
# lista1.append([8,21,10])


# coloca cada elemento da lista como valor adicional à lista
#não aceita valor unico, somente valores iteráveis
# lista1.extend([123,44,67])

#não substitui o valor inicial, o mesmo sera realocado para direita
# lista1.insert(2, 'novo valor') 
# print(lista1)

# para juntar 2 istas

# lista4 = lista1 + lista2
# print(lista4)
# print(lista1)

# lista1.extend(lista2)
# print(lista1)

# para imprimir a lista inversa
# lista1.reverse()
# lista2.reverse()
# print(lista1)
# print(lista2)

# ou a de baixo

# print(lista1[::-1])
# print(lista2[::-1])

# copiar uma lista
# lista4 = lista2.copy()

# para decobrir o tamanho da lista é so usar o len e pasar como parametro a lista
# print(len(lista1))

# podemos remover Facilmente o ultimo elemento de uma lista
# o pop não somente remove o ultimo elemento como retorna
lista3.pop()

# podemos remover um elemento pelo ìndice
# é só passar o index como parametro
# se não tivermos item no index indicado será retornado um index.error
lista1.pop(2)
print(lista1)

# podemos remover todos os itens de uma lista
lista1.clear()
print(lista1)

# podemos repetirelementos m uma lista
lista1 = 'nova' * 3
print(lista1)

# podemos facilmente converter uma string para uma lista

curso = ' transformando um string em uma lista'
curso = curso.split()
print(curso)
para mudar o parametro do split, é só passar le no meio dos parenteses
curso = 'programação,em,python,essencial'
print(curso)
curso = curso.split(',')
print(curso)

# converter uma lista em uma string
# abaixo estamos falando, pega a lista 6 coloca um espaço e transforma em uma string
lista6 = ['programação', 'em', 'python', 'essencial']
curso = ' '.join(lista6)
print(curso)

# iterando sobre listas 

# exemplo1
soma = ''
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(soma)

# exemplo 2 - utilizando while


carrinho = []
produto = ''

while produto != 'sair':
    print('adicione um produto na lista ou digite "sair" para sair; ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# utilizando variáveis em listas

numeros = [ 1, 2, 3 , 4 , 5]
print(numeros)
num1 = 1
num2 = 2
num3 = 3 
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# em lista fazemso acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'Branco']

print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# fazer a busca de forma inversa

print(cores[-1]) #Branco 

# gerar indices em um for
cores = ['verde', 'amarelo', 'azul', 'Branco']

for indice, cor in enumerate(cores):
    print(indice,cor)

# encontrar um indice em uma lista
#passando por parametro o valor
# caso não tenha este numero na lista le vai retornar um Value error


print(numeros.index(10))

# podemos fazer busca dentro de um range, ou seja qual indice comecar a buscar
numeros = [5,6,7,5,8,9,10]

print(numeros.index(8, 3, 6))


# lista[inicio :fim :passo]

# trabalhando com slice de lista com o parametro de 'inicio'

lista = [1,2,3,4]
print(lista[1:])

# trabalhando com slice de lista com o parametro de 'Fim'
print(lista[:3])

# trabalhando com slice de lista com o parametro 'passo'


print(lista[1:: ])


# soma , valor maximo, valor minimo,tamanho
# se os valores forem todos numeros inteiros ou reais 
lista = [1,2,3,4,5,6]

print(sum(lista)) #soma
print(max(lista)) #maximo valor
print(min(lista)) #minimo valor
print(len(lista)) #tamanho da lista

#  transformar uma lista em tupla

lista = [1,2,3,4,5,6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# desmpacotamento de listas
# se tivermos mais valores do que quantidades de variávis para desempacotar, retornará um value error
lista = [1,2,3,4]

num1 , num2, num3 = lista

print(num1)
print(num2)
print(num3)


# copiando uma lista para outra(shallow copy e deep copy)

lista = [1,2,3]

nova  = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# veja que ao utilizarmos lista.copy() copiamos os dados da outra lista, mas eles ficaram totalmente independentes, 
# isto em python se chama deep copy (copia profunda)

# form 2 - shallow copy

lista = [1,2,3]
print(lista)
nova = lista #copia

print(nova)

nova.append(4)

print(lista)
print(nova)

#  veja que utilizamos a copia via atribuição, copiamos os dados da lista para a nova lista, mas após utilizarmos modificação em uma lista
# se refletiu em ambas as listas em python se chma shalow copy

"""

lista1 = [ 1,7,2 ,5 ,3 , 6 ,4]

lista2 = ['l','i','s','t','a','d','e',' ','s','t','r','i','n','g','s']

lista3 = list(range(11))

# outros metodos não tão importantes, mas uteis
