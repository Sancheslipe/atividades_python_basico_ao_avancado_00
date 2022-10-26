def hipotenusa(a,b):
    resp = ((float(a)**2) + (float(b)**2))** 0.5
    return resp


a = input(' digite o numero referente ao cateto A: ')
if a .replace('.','', 1).replace('-','').isdigit():
    a  = float(a)

    b = input(' digite o numero referente ao cateto B: ')
    if b.replace('.','', 1 ).replace('-','').isdigit():
        b = float(b)

        print(f' a hipotenumsa é {hipotenusa(a,b)}')
    
    
    else:
        print('digite um numero válido')



else:
    print('digite um numero válido')