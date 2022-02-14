lista = []
for v in range (0, 5):
    lista.append(int(input('Digite um valor: ')))

menor = maior = lista[0]
for e in lista:
    if e > maior:
        maior = e
    if e < menor:
        menor = e
print(lista)
print(f'O maior valor digitado foi o {maior} na posição {lista.index(maior)}.'
      f'\nO menor valor digitado foi o {menor} na posição {lista.index(menor)}.')
