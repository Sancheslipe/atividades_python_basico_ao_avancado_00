quantidadeNota100 = 0 
quantidadeNota50 = 0
quantidadeNota20 = 0
quantidadeNota10 = 0
quantidadeNota5 = 0 
quantidadeNota2 = 0
quantidadeMoeda1 = 0
quantidadeNotas = 0

 
saque = input('digite o valor do saque ')


if saque.replace(".", "", 1).isdigit():
    saque = float(saque)
    resto = saque

    if saque // 100:        
        quantidadeNota100 = saque // 100
        
        saque = saque - (quantidadeNota100 * 100)
        resto = resto - saque
    
    if (resto > 0.0) and resto % 50 == 0 :
        quantidadeNota50 = saque // 50
        
        saque = saque - (quantidadeNota50 * 50)
        resto = resto - saque
        
    
    if (resto > 0.0) :
        quantidadeNota20 = saque // 20
        
        saque = saque - (quantidadeNota20 * 20)
        resto = resto - saque
    
    if (resto > 0.0) : 
        quantidadeNota10 = saque // 10
        
        saque = saque - (quantidadeNota10 * 10)
        resto = resto - saque
    
    if (resto > 0.0):
        quantidadeNota5 = saque // 5
    
        saque = saque  - (quantidadeNota5 * 5 )
        resto = resto - saque
    
    if (resto > 0.0):
        quantidadeNota2 = saque // 2
    
        saque = saque - (quantidadeNota2 * 2 )
        resto = resto - saque
    
    if (resto > 0.0):
        quantidadeMoeda1 = saque // 1
    
        saque = saque - (quantidadeMoeda1 )
        resto = resto - saque
    
    
        
    print(f'quantidade de notas de R$100,00 |{quantidadeNota100}')
    print(f'quantidade de notas de R$50,00 |{quantidadeNota50}')
    print(f'quantidade de notas de R$20,00 |{quantidadeNota20}')
    print(f'quantidade de notas de R$10,00 |{quantidadeNota10}')
    print(f'quantidade de notas de R$5,00 |{quantidadeNota5}')
    print(f'quantidade de notas de R$2,00 |{quantidadeNota2}')
    print(f'quantidade de moedas de R$1,00|{quantidadeMoeda1}')

else:
    print('digite um valor válido')

