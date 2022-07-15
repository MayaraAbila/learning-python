def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não digitar o número\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não digitar o número\033[m')
            return 0
        else:
            return n


num = leiaInt('Número inteiro: ')
nfloat = leiaFloat('Número Real: ')
print(f'Os números digitados foram: {num} e {nfloat}.')
