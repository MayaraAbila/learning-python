from random import randint
from time import sleep

numero = randint(0, 5)
#print(numero)

print('Estou escolhendo um número...')
sleep(2)

adivinhar = int(input('Tente adivinhar o número escolhido: '))
print('Processando...')
sleep(2)


if adivinhar == numero:
    print('Você acertou!')
else:
    print('Você errou! O número certo era o {}.'.format(numero))
