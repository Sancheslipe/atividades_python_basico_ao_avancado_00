maior = 0 
num = 0
numReverso = 0
a = 100
b = 100
palindromo = 0

while a <= 998:
    
    while b <= 998:
        b = b + 1
        a  = a +1
        num = a * b
        num = str(num)
        
        if num == num[:: -1]:
            palindromo = int(num)
            if palindromo > maior:
                maior = palindromo

print(f' o maior palindromo entre dois numeros de 3 digitos é {maior}')