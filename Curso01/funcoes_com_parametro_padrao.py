def mostra_informacao(nome, instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek'
    elif nome == 'Geek':
        return ' Eu pensei que você era o instrutor'
    return f'olá {nome}'

print(mostra_informacao('Geek',True))


"""
#variáveis globais

#vaiáveis locais

instrutor = 'Geek' #variável global

#obs: se tiver uma variável local com o mesmo nome de uma variável global, a local terá preferência.


#ATENÇÃO evite váriaveis globais

"""