pessoa = []
grupo = []
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    grupo.append(pessoa[:])  # copia e não ligação entre as listas
    pessoa.clear()
    cont = str(input('Quer continuar [S/N]? ')).lower()
    if cont == 'n':
        break
print(f'Foram cadastradas {len(grupo)} pessoas.')
for p in grupo:
    if p[1] >= 100:
        print(f'As pessoas mais pesadas são: ')
        print(f'{p[0]}')
    else:
        print(f'As pessoas mais leves são: ')
        print(f'{p[0]}')
