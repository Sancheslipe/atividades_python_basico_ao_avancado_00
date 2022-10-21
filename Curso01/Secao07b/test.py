x = [
    [1, 2], 
    [3, 4], 
    [5, 6]
    ]

for index, lista in enumerate(x):
    for index, value in enumerate(lista):
        print(value)
        if value < 4:
            lista[index] = 1

print(x)