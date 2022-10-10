altura = float(input('digite a altura'))
baseMaior = float(input('digite o tamanho da base maior'))

if baseMaior > 0 :
    baseMenor = float(input('digite o tamanho da base menor')) 
    if baseMenor > 0 :
        areaTrapezio = ((baseMaior + baseMenor)* altura ) / 2
        print(f' a area do trapézio é de {areaTrapezio}')

    else:
        print('a base menor tem que ser menor do que zero')

else:
    print(' a base maior precisa ser maior que zero')

