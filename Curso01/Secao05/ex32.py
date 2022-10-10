codigo = input('digite o código')
quantidade = int(input('digite a quantidade do produto'))
produto = ''
valor = 0.000 

if codigo == '100':
    produto = 'Cachorro Quente'
    valor =  1.20 * quantidade 
elif codigo == '101':
    produto = 'Bauru Simples'
    valor = 1.30 * quantidade
elif codigo == '102':
    produto = 'Bauru Com Ovo'
    valor = 1.50 * quantidade         
elif codigo == '103':
    produto = 'Hamburguer'
    valor =  1.20 * quantidade              
elif codigo == '104':
    produto = 'Chese Burguer'
    valor = 1.70 * quantidade                  
elif codigo == '105':
    produto = 'Suco'
    valor = 2.20 * quantidade                     
elif codigo == '106':
    produto = 'Refrigerante'
    valor = 1.00 * quantidade
    print(f' o produto é {produto}')
    print(valor,' é o valor do protuto')


print(f' você escolheu {quantidade} {produto} O valor total ficou R${valor}')