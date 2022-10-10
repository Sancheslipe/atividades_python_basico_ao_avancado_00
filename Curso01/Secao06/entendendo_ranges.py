"""
- precisamos conhecer o loop for para entender o loop ranges
- precisamos conhecer o range para trabalhar melhor com o for

Ranges são utilizados para gerar sequencias numericas, não de forma aleatória,
mas sim de maneira simplificada

formas gerais:

forma # 1
range(valor_de_parada)
for _ in range(11):
    print(_)

OBS: Valor_de_parada não inclusive inicio padrao 0, e passo de 1 em 1 

forma # 2

range(valor_de_inicio,Valor_de_parada)
for num in range(1, 11):
    print(num)

forma # 3
range(valor_de_inicio, valor_de_parada, passo)
OBS: Valor_de_parada não inclusive inicio específicado pelo usuário e passo específicado pelo usuário 
for num in range(5,50, 5):
    print(num)


forma # 4
(inverso do 3)
range(valor_de_inicio, valor_de_parada, passo)

for num in range(10,-5, -1):
    print(num)

OBS: Valor_de_parada não inclusivo( valor inicio específicado pelo usuário e passo específicado pelo usuário 
"""

for num in range(10,-5, -1):
    print(num)