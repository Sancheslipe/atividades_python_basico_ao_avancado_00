salario = float(input('Digite o seu salário'))
parcela = float(input('digite o valor da prestação do emprestimo'))

valorParcela = parcela * 100
porcentagemParcela = (valorParcela / salario) / 100

if porcentagemParcela > 0.2 :
    print('Empréstimo não concedido')
else:
    print('Empréstimo Concedido')
