valorHora = float(input('digite o valor da hora de trabalho (em reais)')) 
horas = float(input('digite as horas trabalhadas '))

valorTotal = (horas * valorHora) + ((horas * valorHora) * 0.1)

print(f' O valor total de horas é de R${valorTotal} ')
