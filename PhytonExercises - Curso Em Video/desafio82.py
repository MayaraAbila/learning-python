completa = []
pares = []
impares = []
while True:
    completa.append(int(input('Digite um valor: ')))
    cont = str(input('Quer continuar [S/N]? ')).lower()
    if cont == 'n':
        break
for num in completa:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(completa)
print(pares)
print(impares)