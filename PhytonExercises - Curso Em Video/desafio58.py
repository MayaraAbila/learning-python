from random import randint
from time import sleep

numero = randint(0, 10)
print(numero)
print('Estou escolhendo um número...')
sleep(2)

adivinhar = int(input('Tente adivinhar o número escolhido: '))
sleep(1)

tentativas = 0
while numero != adivinhar:
    sleep(1)
    print('Processando...')
    sleep(1)
    print('\033[1;31mVocê não acertou! Tente novamente')
    adivinhar = int(input('\033[0;0mTente adivinhar o número escolhido: '))
    tentativas += 1

if tentativas == 0:
    print((f'\n\033[1;32mVocê acertou o número ({numero}) na primeira tentativa!'))
else:
    print(f'\n\033[1;32mVocê acertou o número ({numero}) e precisou de {tentativas} tentativas.')