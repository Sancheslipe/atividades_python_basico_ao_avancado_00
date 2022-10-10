custoDeFabrica = float(input(' Digite o custo de fabrica do carro'))
custoConsumidor = 0

if custoDeFabrica <= 12000:
    custoConsumidor = (custoDeFabrica * 0.05) + custoDeFabrica
elif custoDeFabrica >= 12001 and custoDeFabrica <= 25000:
    custoConsumidor = (custoDeFabrica * 0.10) + (custoDeFabrica * 0.15) + custoDeFabrica
elif custoDeFabrica >25000:
    custoConsumidor = (custoDeFabrica * 0.15) + (custoDeFabrica * 0.20) + custoDeFabrica

print(f' o custo ao consumidor será de {custoConsumidor}')
  