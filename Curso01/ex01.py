num = input('digite um numero inteiro: ')
if num.isdigit():
    num = int(num)


def dobro(num):
    dobro = num * 2
    return dobro

print(f'o dobro é {dobro(num)}')
