import locale


def monetario(num, p=True):
    if p == False:
        return num
    else:
        locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
        num = locale.currency(num, grouping=True)
        return num


def aumentar(num, aum, p=True):
    num = num + (num * (aum/100))
    if p == False:
        return num
    else:
        return monetario(num)


def reduzir(num, red, p=True):
    num = num - (num * (red/100))
    if p == False:
        return num
    else:
        return monetario(num)


def dobro(num, p=True):
    num = num*2
    if p == False:
        return num
    else:
        return monetario(num)


def metade(num, p=True):
    num = num/2
    if p == False:
        return num
    else:
        return monetario(num)


def resumo(num, aum, red):
    print('--'*17)
    print('       \033[1;32mResumo do Valor\033[0;0m      ')
    print('--'*17)
    print(f'Preço Analisado: \t{monetario(num)}')
    print(f'Dobro do Preço: \t{dobro(num)}')
    print(f'Metade do Preço: \t{metade(num)}')
    print(f'{aum}% de aumento: \t{aumentar(num, aum)}')
    print(f'{red}% de redução: \t{reduzir(num, red)}')
    print('--'*17)
