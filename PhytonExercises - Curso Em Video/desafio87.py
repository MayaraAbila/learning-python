matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para: [{l}, {c}]: '))
print(matriz[0])
print(matriz[1])
print(matriz[2])
par = soma3c = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
for v in range(0, 3):
    soma3c += matriz[v][2]
for v in range(0, 3):
    if v == 0:
        maior = matriz[1][v]
    elif matriz[1][v] > maior:
        maior = matriz[1][v]
print(f'A soma dos valores pares digitados é de: {par}')
print(f'A soma dos valores da terceira coluna é de: {soma3c}')
print(f'O maior valor da segunda linha é de: {maior}')
