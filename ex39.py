salario = float(input('digite o seu salário '))
tempoDeServico = float(input('digite o seu tempo de serviço nesta empresa '))
novoSalario = 0

if salario <= 500:
    if tempoDeServico < 1 :
        novoSalario = (salario * 0.25) + salario
    elif tempoDeServico >= 1 and tempoDeServico <= 3:
        novoSalario = (salario * 0.25) + salario + 100
    elif tempoDeServico >= 4 and tempoDeServico <=6:
        novoSalario = (salario * 0.25 ) + salario + 200
    elif tempoDeServico >= 7 and tempoDeServico <=10:
        novoSalario = (salario * 0.25) + salario + 300
    elif tempoDeServico > 10:
        novoSalario = (salario * 0.25) + salario + 500
elif salario > 500 and salario <= 1000:
    if tempoDeServico < 1 :
        novoSalario = (salario * 0.20) + salario
    elif tempoDeServico >= 1 and tempoDeServico <= 3:
        novoSalario = (salario * 0.20) + salario + 100
    elif tempoDeServico >= 4 and tempoDeServico <=6:
        novoSalario = (salario * 0.20 ) + salario + 200
    elif tempoDeServico >= 7 and tempoDeServico <=10:
        novoSalario = (salario * 0.20) + salario + 300
    elif tempoDeServico > 10:
        novoSalario = (salario * 0.20) + salario + 500
elif salario > 1000 and salario <= 1500:
    if tempoDeServico < 1 :
        novoSalario = (salario * 0.15) + salario
    elif tempoDeServico >= 1 and tempoDeServico <= 3:
        novoSalario = (salario * 0.15) + salario + 100
    elif tempoDeServico >= 4 and tempoDeServico <=6:
        novoSalario = (salario * 0.15 ) + salario + 200
    elif tempoDeServico >= 7 and tempoDeServico <=10:
        novoSalario = (salario * 0.15) + salario + 300
    elif tempoDeServico > 10:
        novoSalario = (salario * 0.15) + salario + 500
elif salario > 1500 and salario <= 2000:
    if tempoDeServico < 1 :
        novoSalario = (salario * 0.10) + salario
    elif tempoDeServico >= 1 and tempoDeServico <= 3:
        novoSalario = (salario * 0.10) + salario + 100
    elif tempoDeServico >= 4 and tempoDeServico <=6:
        novoSalario = (salario * 0.10 ) + salario + 200
    elif tempoDeServico >= 7 and tempoDeServico <=10:
        novoSalario = (salario * 0.10) + salario + 300
    elif tempoDeServico > 10:
        novoSalario = (salario * 0.10) + salario + 500
elif salario > 2000:
    if tempoDeServico < 1 :
        print(f'você não tem direito a aumento!')
        novoSalario =  salario 
    elif tempoDeServico >= 1 and tempoDeServico <= 3:
        novoSalario = salario + 100
    elif tempoDeServico >= 4 and tempoDeServico <=6:
        novoSalario =  salario + 200
    elif tempoDeServico >= 7 and tempoDeServico <=10:
        novoSalario = salario + 300
    elif tempoDeServico > 10:
        novoSalario = salario + 500

print(f'O seu salário é R${novoSalario} ')