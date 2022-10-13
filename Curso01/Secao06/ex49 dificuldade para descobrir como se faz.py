
carlos = int(input("digite o salario de joão"))
joao = carlos/3
mes = 0

while joao <= carlos:
    carlos = carlos + (carlos * 0.02)
    joao = joao + (joao * 0.05)

    mes = mes + 1

print(f' o numero de meses necessários para joão pasar carlos é {mes}, Total de carlos {carlos}, total de joão {joao}')

