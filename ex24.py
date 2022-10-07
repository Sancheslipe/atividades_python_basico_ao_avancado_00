valor = float(input(' digite o valor do produto'))
estado = input('digite:\n[MG] para Minas gerais\n[SP] Para são paulo\n[RJ] para Rio de Janeiro\n[MS] para Mato groso do sul\nSigla do estado:')


if estado == 'MG'or estado == 'SP' or estado == 'RJ' or estado == 'MS':


    if estado == 'MG':
        print(f' o Valor do produto para o Seu estado é R${(valor * 0.07) + valor}')


    if estado == 'SP':
        print(f' o Valor do produto para o Seu estado é R${(valor * 0.12) + valor}')


    if estado == 'RJ':
        print(f' o Valor do produto para o Seu estado é R${(valor * 0.15) + valor}')


    if estado == 'MS':
        print(f' o Valor do produto para o Seu estado é R${(valor * 0.08) + valor}')

else:
    print(' você digitou um estado não válido')