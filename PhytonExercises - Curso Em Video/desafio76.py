produtos = ('Macarrão', '4.50', 'Pão', '6.00', 'Mussarela', '7.50', 'Amaciante', '8.90', 'Sabão em pó', '10.00')

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R$ {produtos[pos]:>5}')
