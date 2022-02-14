lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = str(input('Quer continuar [S/N]? ')).lower()
    if cont == 'n':
        break
print(f'Foram digitados {len(lista)} valores.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}')
if 5 in lista:
    print(f'O valor 5 esta na lista na posição {lista.index(5)}.')
else:
    print('O valor 5 não foi digitado!')