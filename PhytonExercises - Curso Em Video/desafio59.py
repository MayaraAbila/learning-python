from time import sleep
int1 = int(input('Digite o primeiro valor: '))
int2 = int(input('Digite o segundo valor: '))
sleep(1)
opçao = 0

while opçao != 5:
    print('\n\033[;1m----MENU----')
    opçao = int(input('Escolha a operação que deseja: '
                      '\n[1] Somar'
                      '\n[2] Multiplicar'
                      '\n[3] Maior'
                      '\n[4] Novos números'
                      '\n[5] Sair do programa: '))
    if opçao == 1:
        print(f'\033[1;32mA soma dos dois números é: {int1+int2}')
    elif opçao == 2:
        print(f'\033[1;32mA multiplicação entre os dois números é: {int1*int2}')
    elif opçao == 3:
        if int1 > int2:
            print(f'\033[1;32mO maior número digitado é o {int1}')
        else:
            print(f'\033[1;32mO maior número digitado é o {int2}')
    elif opçao == 4:
        int1 = int(input('Digite o primeiro valor: '))
        int2 = int(input('Digite o segundo valor: '))
    elif opçao == 5:
        print('Encerrando...')
        sleep(1)
    else:
        print('Número invalido, digite novamente!')

print('\n\033[1;34mPrograma Finalizado!')
