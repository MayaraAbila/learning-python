def validar(num):
    num = num.replace(',', '.')
    while num.isalpha() == True or num.strip() == '':
        num = input(
            f'\033[1;31mErro: "{num}" é um preço invalido!\033[0;0m Digite novamente: ')
    return float(num)
