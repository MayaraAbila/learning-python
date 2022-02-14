s = 0
for c in range(6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        s += num
print(f'A soma dos valores digitados, que são pares é: {s}')
