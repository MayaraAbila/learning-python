tot = cont = preço = 0
barato = 100000000
produto1 = 's'

while True:
    produto = str(input('Qual o produto? '))
    preço = float(input('Qual o preço do produto? '))
    continuar = str(input('Você quer continuar [S/N]? ')).lower()
    if preço > 1000:
        cont += 1
    if preço < barato:
        produto1 = produto
    tot += preço
    if continuar == 'n':
        break
print('=--'*20)
print(f'O total gasto foi de R${tot:,.2f}'
      f'\n{cont} produtos custam mais que R$1.000'
      f'\nO produto mais barato foi o/a {produto1}.')
