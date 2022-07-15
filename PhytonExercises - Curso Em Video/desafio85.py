# criar listas dentro de listas sem precisar nomea-las
numeros = [[], []]
for c in range(0, 6):
    num = int(input(f'Digite o {c+1} valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
# numeros.append(pares[:])
# numeros.append(impares[:])
print(numeros)
