def escreva(txt):
    # transformei cada caractere em uma nova tupla pra medir o tamanho dela corretamente
    #tamanho = len(tuple(f'{txt}'))
    tamanho = len(txt)
    print('-'*tamanho)
    # se imprimir sem o 0, vira a tupla da forma declarada e não somente o valor
    print(txt)
    print('-'*tamanho)


escreva('Mayara Tolentino Abila')
escreva('Estudante de Python')
escreva('no Curso em Video')
