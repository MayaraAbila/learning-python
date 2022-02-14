from random import randint
num = pc = validação = 0
parimpar = 'p'
espaço = ('\033[1;37m=-\033[0;0m'*15)

print('Vamos jogar PAR ou Ímpar!')

while True:
    num = int(input('Digite um valor: '))
    parimpar = str(input('Par ou Ímpar? [P/I]: ')).lower().strip()[0] #pegar somente a primeira letra digitado - caso o usuário digite por extenso
    print(f'{espaço}')
    pc = randint(0, 10)
    validação = num + pc
    if parimpar == 'p':
        if validação % 2 == 0:
            print(f'\033[1;36mO computador jogou {pc} e você {num}. DEU PAR! Você \033[1;92mGANHOU!\033[0;0m')
        else:
            print(f'\033[1;36mO computador jogou {pc} e você {num}. DEU ÍMPAR! Você \033[1;31mPERDEU!\033[0;0m')
            print(f'{espaço}')
            print('GAME OVER!')
            break
    elif parimpar == 'i':
        if validação % 2 > 0:
            print(f'\033[1;36mO computador jogou {pc} e você {num}. DEU IMPAR! Você \033[1;92mGANHOU!\033[0;0m')
        else:
            print(f'\033[1;36mO computador jogou {pc} e você {num}. DEU PAR! Você \033[1;31mPERDEU!\033[0;0m')
            print(f'{espaço}')
            print('GAME OVER!')
            break
    print('Vamos Jogar novamente..') #ñ preciso colocar dentro do while, pq o programa ñ vai para enquanto o usuário não perder
    print(f'{espaço}')


