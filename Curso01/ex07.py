def conversor_celsios_to_fahrenheit(celsius):
    
    fahrenheit = float(celsius) * (9/5) + 32
    return fahrenheit


temp = input('digite uma temperatura em graus celsius: ')
if temp.replace('.','', 1).replace('-','').isdigit():
    temp = float(temp)
    
    print(f' a temperatura {temp} em graus celsius fica {conversor_celsios_to_fahrenheit(temp)} en farenheit')



else:
    print('digite uma temperatura válida')