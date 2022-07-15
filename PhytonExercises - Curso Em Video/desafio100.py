from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando valores...')
    sleep(1)
    for c in range(0, 5):
        numeros.append(randint(1, 10))
    print(f'Os números sorteados foram {numeros}')
    return(numeros)


def somaPar(lista):
    print('--'*20)
    sleep(1)
    soma = 0
    for v in numeros:
        if v % 2 == 0:
            soma += v
    print(f'A soma dos números pares em {numeros} totaliza {soma}.')


numeros = []
sorteia(numeros)
somaPar(numeros)
