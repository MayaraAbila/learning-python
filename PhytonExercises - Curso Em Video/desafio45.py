from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

jogador = int(input('Suas opções \n'
                    '0 - Pedra \n'
                    '1 - Papel \n'
                    '2 - Tesoura \n'
                    'Qual é a sua jogada? '))

computador = randint(0, 2)

print('-=' * 10)
sleep(1)
print('JO\n')
sleep(2)
print('KEN \n')
sleep(2)
print('PÔ!\n')
sleep(1)
print('-=' * 10)

sleep(1)
print(f'Computador jogou: {itens[computador]}')
sleep(1)
print(f'Jogador jogou: {itens[jogador]}')
#acessei a lista e a partir dos inputs, busquei o objeto de acordo com a posição gerada
sleep(1)

if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE!')

    elif jogador == 1: #papel
        print('JOGADOR VENCEU!')

    else: #tesoura
        print('COMPUTADOR VENCEU!')

if computador == 1: #papel
    if jogador == 1:
        print('EMPATE!')

    elif jogador == 0: #pedra
        print('COMPUTADOR VENCEU!')

    else: #tesoura
        print('JOGADOR VENDEU!')

if computador == 2: #tesoura
    if jogador == 2:
        print('EMPATE!')

    elif jogador == 0: #pedra
        print('JOGADOR VENCEU!')

    else: #papel
        print('COMPUTADOR VENCEU!')