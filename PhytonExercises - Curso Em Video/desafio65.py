soma = 0
tot = 0
maior = menor = 0
cont = 'S'

while cont == 'S':
    num = int(input('Digite um número: '))
    soma += num
    tot += 1
    if tot == 1: # se eu digitar uma única vez, ñ haverá comparação e eles assumirão o mesmo numero / independete da quant de numeros digitados, na primeira volta já haverá uma nova atribuição, evitando que o menor numero seja considerado com oq foi declacarado fora do laço de repetiçaõ
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont = str(input('Você quer continuar [S/N]? ')).upper()

print(f'\nMédia dos números: {soma/tot:,.2f}'
      f'\nMaior valor: {maior}'
      f'\nMenor valor: {menor}')
