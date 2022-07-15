def leiaInt(n):
    while n.isnumeric() != True:
        # print(type(n))
        print('\033[1;31mErro! Digite um número inteiro válido\033[0;0m.')
        n = input("Digite um número: ")
    return n


n = leiaInt(input("Digite um número: "))  # input le como string
print(f'Você acabou de digitar o número {n}.')
