def opcao(digito):
    if digito == 2:
        print('--'*15)
        arquivo = open("cadastros.txt", "a")
        nome = input('Nome: ')
        arquivo.write(nome)
        idade = input('Idade: ')
        arquivo.write(idade)
        print(
            f'{nome} foi adicionado ao arquivo "{arquivo.name}", com o modo de acesso "{arquivo.mode.upper()}".')
        arquivo.close()
        opcao(menu())

    if digito == 1:
        print('--'*15)
        print('Pessoas Cadastradas')
        print('--'*15)
        arquivo = open("cadastros.txt", "r")
        print(arquivo.readlines())
        opcao(menu())

    while digito == 3:
        print('--'*15)
        print('\033[1;31mVolte Sempre!')
        break


def menu():
    print('--'*15)
    print('\033[1;34mMenu Principal')
    print('\033[0;0m--'*15)
    print('\033[1;34m1 - Ver Pessoas Cadastradas')
    print('2 - Cadastrar nova Pessoas')
    print('3 - Sair do Sistema\033[0;0m')
    print('--'*15)
    digito = int(input('Sua Opção: '))
    return digito


opcao(menu())
