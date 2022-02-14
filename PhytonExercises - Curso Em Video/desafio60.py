#---------utilizando modulo--------
#from math import factorial
#num = int(input('Digite um número: '))
#f = factorial(num)
#print(f'O fatorial de {num} é {f}.')

#--------forma matematica

n = int(input('Digite um número: '))
c = n
f = 1 #fator nulo de multiplicação
print(f'Calculando {n}! ...')
while c > 0:
    print(f'{c}', end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c #salvar a multiplicação do fatorial
    c -= 1
print(f'{f}')


