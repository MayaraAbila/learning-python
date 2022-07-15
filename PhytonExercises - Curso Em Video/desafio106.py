def Help():
    while True:
        f = str(input('Função ou Biblioteca: '))
        if f.upper() == 'FIM':
            break
        else:
            print(help(f))
            break


Help()
