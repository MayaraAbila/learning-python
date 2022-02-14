#PROGRESSAO ARITMETICA: Uma progressão aritmética é uma sequência numérica em que cada termo, a partir do segundo, é igual à soma do termo anterior com uma constante r. O número r é chamado de razão ou diferença comum da progressão aritmética.
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1

while cont <= 10:
    print(f'{termo}', end=' > ')
    termo += razão
    cont += 1
print('Fim')

