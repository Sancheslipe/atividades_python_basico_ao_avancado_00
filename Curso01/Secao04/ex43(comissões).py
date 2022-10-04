valor = float(input('Digite o valor Total'))

print(f' o valor total com desconto de 10% é R${ valor - (valor * 0.1) }')
print(f' o valor de cada parcela (3x sem juros) R${valor / 3}')
print(f' O valor da comissão (caso a venda seja com desconto de 10%) R${(valor - (valor * 0.1)) * 0.05 }')
print(f' O valor da comissão caso a venda seja parcelada R${valor * 0.05}')