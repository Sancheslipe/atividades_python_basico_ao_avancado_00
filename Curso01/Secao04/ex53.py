comprimento = int(input('digite o comprimento do terreno !'))
largura = int(input('digite a largura '))

preco = int(input('digite o preço '))


calculoArea = comprimento * largura

calculoPreco = preco * calculoArea


print(f' esta é a area {calculoArea} e este é o preço que irá custa as cercas com tela {calculoPreco}')