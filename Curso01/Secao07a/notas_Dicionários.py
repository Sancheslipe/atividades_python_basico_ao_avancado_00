# """
# dicionarios

# OBS: em algumas linguagns de programação os dicionários python são conhecidos por mapas

# dicionários são do tipo chave : valor
# dicionários são representados por chaves


# print(type({}))

# OBS: sobre dicionários 
#     - chave e valor são separados por dois pontos 'chave : valor'
#     - tanto chave quanto valor podem ser de qualquer tipo de dados >
#     - podemos misturar tipos de dados:

# # criação de dicionários
# #forma 1 (mais comum)
# paises = {'br': 'Brasil', 'eua' : 'Estados Unidos', 'py' : 'Paraguai'}

# paises = {'br': 'Brasil', 'eua' : 'Estados Unidos', 'py' : 'Paraguai'}
# print(paises)
# print(type(paises))

# #2 forma (menos comum)

# paises = dict(br = 'Brasil', ua='Estador Unidos', py='paraguai')
# print(paises)
# print(type(paises))


# paises = {'br': 'Brasil', 'eua' : 'Estados Unidos', 'py' : 'Paraguai'}

# #Acessando Elementos

# #forma 1 - acessando via chave, d memsa forma que lista, tupla
# print(paises['br'])
# #print(paises['ru'])

# #caso tentamos fazer um acesso de uma chave inexistente teremos um key error

# #forma 2 (forma recomendada) - acessando via get

# print(paises.get('br'))
# print(paises.get('ru'))
# #caso tentamos fazer um acesso de uma chave ineistente desta maneira, ele retorna None (tipoo sem tipo)

# russia = paises.get('py')

# if russia:
#     print('Encontei o pais')
# else:
#     print('não encontrei')

# #adicionar itens em um dicionário

# receita = { 'jan' : 100, 'fev' : 120, 'mar' : 300}
# print(receita)
# print(type(receita))

# #forma 1

# receita['abr'] = 350

# print(receita)

# #forma 2 

# novo_dado = {'mai' : 500}

# receita.update(novo_dado)

# print(receita)

# #atualizando dados em um dicionário


# receita['mai'] = 550

# print(receita)

# #forma 2 
# receita.update({'mai' : 600})

# print(receita)

# #conclusão 1: a forma de adiconar novos elementos ou atualizar dados em um dicionário é a mesma
# #conclusão 2:  em dicionários, NÃO podemos ter chaves repetidas 

# """
# #Remover dados de um dicionário

# # receita = { 'jan' : 100, 'fev' : 120, 'mar' : 300}
# # print(receita)

# # #forma #1
# # ret = receita.pop('mar')
# # print(ret)

# # print(receita)

# # #OBS: aqui precisamos sempre informar a chve, e caso não encontre o elemento , um KeyErrror é retornado.
# # #OBS 2: ao removermos um objeto o valor deste objeto é sempre retornado.

# # #forma 2 

# # del receita['fev']

# # print(receita)

# # se a chave não existir será gerado um KeyError
# #ons: neste caso o valor removido Não é retornado

# #imagine você tem um ecomerce, onde temos um carrinho de compras na qual adicionamos produtos.
# """
# carrinho de compras:
#     produto1:
#         nome;
#         preço;
#         quantidade;
#     produto2;
#         nome; 
#         quantidade;
#         preço;

# #1 poderiamos utilizar lista para isso

# carrinho = []

# produto1 = ['Playstationa 4', 1, 2300.00]
# produto2 = ['God of War 4', 1, 150.00]

# carrinho.append(produto1)
# carrinho.append(produto2)
# print(carrinho)

# # teriamos qe saber qual é o indice de cada informação do produto
# #2 - poderiamos utilizar uma tupla para isso? sim

# produto1 = ('Playstationa 4', 1, 2300.00)
# produto2 = ('God of War 4', 1, 150.00)

# carrinho = (produto1, produto2)

# print(carrinho)

# #3 poderiamso usar um dicionario para isso? sim 

# carrinho = []

# produto1 = {'nome':'Playstation 4','quantidade': 1 , 'preco' : 2300.00}
# produto2 = {'nome':'God of War 4','quantidade': 1 , 'preco' : 150.00}

# carrinho.append(produto1)
# carrinho.append(produto2)
# print(carrinho)

# # metodos de cicionários

# d = dict(a = 1, b=2, c=3 )
# print(d)
# print(type(d))

# #limpar o dicionário(zerar dados)

# d.clear()

# print(d)

# #copiando um dicionário para outro

# #forma 1 (deep copy)
# novo = d.copy()

# print(novo)

# novo['d'] = 4
# print(d)
# print(novo)

# #forma2 (shallow copy)

# novo = d 
# print(novo)

# novo['d'] = 4

# print(d)
# print(novo)

# """
# #forma não usual de criação de dicionários

# outro = {}.fromkeys('a','b')
# print(outro)
# print(type(outro))

# usuario = {}.fromkeys(['nome', 'pontos','email','profile'], 'Desconhecido')
# print(usuario)
# print(type(usuario))

# #O metodo from keys recebe 2 parametros : 1 iteravel e um valor
# #ele vai gerar para cada valor do iteravel uma chave e irá retribuir a esta chave o valor informado.

# veja = {}.fromkeys('teste', 'valor')
# print(veja)

# veja = {}.fromkeys(range(1,11), 'novo')

# print(veja)