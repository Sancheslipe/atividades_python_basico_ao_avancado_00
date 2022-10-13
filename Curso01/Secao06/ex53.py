num = input(' digite um numero inteiro')
if num.isdigit():
    num = int(num)
    i = 1
    for c in range(1, num +1):
        for x in range(1, c +1):
            print(i, end =' ')
            i = i + 1
        print()



else:
    print('digite um numero válido')