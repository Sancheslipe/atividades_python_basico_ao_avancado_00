idade = int(input('digite a idade do nadador'))

if idade >= 5 and idade <= 7 :
    print(f'Infantil A {idade} anos')
elif idade >= 8 and idade <= 10 :
    print(f'Infantil B {idade} anos')
elif idade >= 11 and idade <= 13 :
    print(f'Juvenil A {idade} anos')
elif idade >= 14 and idade <= 17 :
    print(f'Juvenil B {idade} anos')
elif idade > 18:
    print(f'Sênior {idade} anos')