# Estrutura de dados composta : tuplas(), listas[], dicionário {}

# RELEMBRANDO LISTAS (indices numericos)
dados = list()  # variavel com uma lista de valores
dados.append('Daniele')
dados.append(28)
print(dados[0])
print(dados[1])

# DICIONARIOS{} - Personalizar os indices de forma literal
dados2 = dict()
dados2 = {'nome': 'Mayara', 'idade': 24}
# dados nome, e dados idade
# indice nome, indice idade
print(dados2['nome'])
print(dados2['idade'])
dados2['sexo'] = 'M'  # adicionar o elemento M no indice sexo
del dados2['idade']
print(dados2)

print('\n')

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
         }

print(filme)
print('\n')

# items - vai trazer todas as informações do dicionário. Tanto os values quanto os keys
print('ITEMS')
# ira printar entre [], sendo lista e cada elemento sendo uma tupla ()
print(filme.items())

print('\n')
# values - vai trazer os valores daquele dicionario
print('VALUES')
print(filme.values())

print('\n')
# chaves - vai trazer os 'indices'
print('KEYS')
print(filme.keys())

print('\n')
for k, v in filme.items():
    print(f'O {k} é {v}')

print('\n')
filme['ano'] = '1950'
filme['favorito'] = 'SIM'
print(filme.values())

print('\n')
# É possível criar dicionários dentro de listas
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1]['sigla'])

# dentro do dicionário nós não conseguimos utilizar o artificio de fatiamento, por ex brasil.append(estado[:]) - nos casos em que eu quero criar uma cópia dos dados sem necessariamente criar uma relação entre eles.
# há um método interno do dicionário que se utiliza por ex: brasil.append(estado.copy())

print('\n')
estado = dict()  # dicionário, k, v
brasil2 = list()  # lista
for c in range(0, 3):
    estado['uf'] = str(input('Unid. Fed: '))
    estado['sigla'] = str(input('Sigla: '))
    # estado é um dicionário e será armazenado dentro da lista brasil
    brasil2.append(estado.copy())
print('\n')
for e in brasil2:
    print(e)
for e in brasil2:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')
