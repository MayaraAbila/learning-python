lista = []
n = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: #se for o primeiro valor digitado(primerio laço) ou se o valor
        # digitado for maior que o ultimo elemento da lista, ele vai inserir ao final
        lista.append(n)
        print('Valor adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na posição {pos}')
                break
            pos += 1
print(lista)