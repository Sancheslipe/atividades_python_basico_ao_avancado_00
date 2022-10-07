# distancia = float(input('digite a distância em km'))
# litros = float(input('digite a quantidade de litros de gasolina consumidos'))

kilometrosPorLitro = int(input('digite   '))

if kilometrosPorLitro <= 8:
    print(f'Venda o carro!{kilometrosPorLitro}')
elif kilometrosPorLitro >= 8 and kilometrosPorLitro <= 13 :
    print(f'Econômico! {kilometrosPorLitro}')
elif kilometrosPorLitro >= 14:
    print(f'Super econômico{kilometrosPorLitro}')