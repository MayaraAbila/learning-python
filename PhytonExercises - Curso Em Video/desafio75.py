#val1 = int(input('Digite um valor: '))
#val2 = int(input('Digite um valor: '))
#val3 = int(input('Digite um valor: '))
#val4 = int(input('Digite um valor: '))
#tupla=(val1, val2, val3, val4)

tupla = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))
print(tupla)
print(f'O número 9 apareceu {tupla.count(9)} vezes na tupla')

if 3 in tupla:
    print(f'O numero 3 foi digitado na posição {tupla.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado')

print('Os números digitados que são pares, foram:', end=' ')
for n in tupla: #ele vai printar o elemento da tupla pq utilizei a tupla e não um intervalo, nesse caso n assume o elemento da tupla
    if n % 2 == 0:
        print(f'{n}', end=' ')

