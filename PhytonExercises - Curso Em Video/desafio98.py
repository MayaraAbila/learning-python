from plistlib import InvalidFileException


from time import sleep


def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim}, em passo {passo}.')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += passo
        print('- Fim!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= passo
        print('- Fim!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez:')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
