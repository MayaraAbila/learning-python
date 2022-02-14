from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(tupla)
menor = maior = tupla[0]

for n in tupla: #ele vai printar o elemento da tupla pq utilizei a tupla e não um intervalo, nesse caso n assume o elemento da tupla
    if n < menor:
        menor = n
    if n > maior:
        maior = n

print(f'O menor número é o {menor} e o maior é o {maior}')

#-----------outra possibilidade de verificar maior e menor em python

print(f'O menor número é o {min(tupla)} e o maior é o {max(tupla)}')
