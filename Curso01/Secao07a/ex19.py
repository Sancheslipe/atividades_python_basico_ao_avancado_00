vetor = []
cont = 0
conta = 0
for i in range(0,49 +1):
    conta = (i + 5 * i) % (i + 1)
    vetor.append(conta)

print(vetor)