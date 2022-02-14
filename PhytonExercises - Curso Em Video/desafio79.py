numerica = []
while True:
    num = (int(input('Digite um valor: '))) #salvar o ultimo numero digitado fora da lista para fazer as validações necessárias e poder prosseguir normalmente.
    if num not in numerica:
        numerica.append(num)
    else:
        print('Valor duplicado, não foi adicionado!')
    continuar = str(input('Quer continuar [S/N]? ')).lower()
    if continuar == 'n':
        break
numerica.sort()
print(numerica)
