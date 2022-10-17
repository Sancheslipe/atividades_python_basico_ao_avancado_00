vetor = []
num = 0 
cont = 1
multiplos = []

while cont <= 5:
    num = input('digite um numero')
    if num.replace(".", "", 1).replace("-", "").isdigit():
        num = 