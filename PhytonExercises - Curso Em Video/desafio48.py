s = 0 #acumulador
cont = 0 #contador
for c in range(500):
    if c % 3 == 0 and c % 2 != 0:
        cont += 1
        s += c

print(cont)
print(f'A soma dos valores entre 1 e 500, multiplos de 3 e ímpares é: {s}.')