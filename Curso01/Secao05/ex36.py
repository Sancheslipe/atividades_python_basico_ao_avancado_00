valorVenda = float(input(' Digite o valor da venda'))
comissao = 0

if valorVenda >= 100000:
    comissao = (valorVenda * 0.16) + 700
elif valorVenda < 100000 and valorVenda >= 80000:
    comissao = (valorVenda * 0.14) + 650
elif valorVenda < 80000 and valorVenda >= 60000:
    comissao = (valorVenda * 0.14) + 600
elif valorVenda < 60000 and valorVenda >= 40000:
    comissao = (valorVenda * 0.14) + 550
elif valorVenda <40000 and valorVenda >= 20000:
    comissao = (valorVenda * 0.14) + 500
elif valorVenda < 20000:
    comissao = (valorVenda * 0.14) + 400

print(f' Comissão: R${comissao}')
