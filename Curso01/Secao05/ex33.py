valorAntigo = float(input('digite o valor antigo do produto'))


if valorAntigo <= 50.00:
    precoNovo = (valorAntigo * 0.05) + valorAntigo
elif valorAntigo > 50.00 and valorAntigo <=100.00 :
    precoNovo = (valorAntigo * 0.1) + valorAntigo
elif valorAntigo > 100.00:
    precoNovo = (valorAntigo * 0.15) + valorAntigo

if precoNovo <= 80.00 :
    print(f'Barato')
elif precoNovo > 80.00 and precoNovo <= 120.00 :
    print(f'normal')
elif precoNovo > 120.00 and precoNovo <= 200.00 :
    print(f'caro')
elif precoNovo > 200.00 :
    print(f'Muito Caro')
