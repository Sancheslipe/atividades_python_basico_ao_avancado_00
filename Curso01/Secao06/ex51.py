salario = 2000
ano = 1996
aumento = 0.015
while ano  != 2022:
    salario = salario + (salario * aumento)
    ano = ano + 1
    aumento = aumento * 2

print(f'o salário no ano 2022 será de {salario} e o percentual de aumento é de {aumento}')