numeros = []
pares = []
impares = []
for c in range(0, 6):
    num = int(input(f'Digite o {c+1} valor: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
pares.sort()
impares.sort()
numeros.append(pares[:])
numeros.append(impares[:])
print(numeros)
