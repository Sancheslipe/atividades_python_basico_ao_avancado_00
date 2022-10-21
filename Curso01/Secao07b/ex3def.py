linha = []
coluna = []
num = 0
calculo = 0

for l in range(0,4):
    for c in range(0,4):
        if l == 0:
            print('linha horizontal')
            num = int(input('digite um numero'))
            coluna.append(num)
        coluna= coluna.split()
        linha[c].append(num.copy())
        coluna.clear()

        if l > 0:
            if c == 0:
                
                print('segunda linha primeiro digito')
                num = int(input('digite um numero'))
                coluna.append(num)
            else:
                
                
