chico = 1.50
ze = 1.10
ano = 0
while ze <= chico:
    chico = chico + (chico * 0.02)
    ze = ze + (ze * 0.03)
    ano = ano + 1

print(f' serão necessários {ano}, altura de zé {ze}, altura de chico{chico}')