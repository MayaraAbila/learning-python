from random import randint
from operator import itemgetter
ranking = []
jogador = {}

# for c in range(0, 4):
#    jogadores[f"jogador{c+1}"] = randint(0, 6)
#    grupo.append(jogadores.copy())
# copio o dicionário gerado para dentro de uma lista
#    jogadores = {}
# limpo o dicionário, para que uma nova chave seja criada sem a informação da anterior. Caso não haja essa ação, sendo um único dicionário, a nova chave o valor serão novamente adicionados dentro da lista.
# print(grupo)

for c in range(0, 4):
    jogador[f'jogador{c+1}'] = randint(1, 6)

for k, v in jogador.items():
    print(f'{k} tirou {v} no dado.')
print('-'*20)
# print(jogador)

ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
# print(ranking)  # tuplas dentro da lista ranking
# crio uma lista para usar a ordenação pelo item 1 - tratado aqui como lista, seria o valor do dado. E reverse para ser em ordem decrescente.

for i, v in enumerate(ranking):  # lista ranking com tuplas
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
# para cada laço, imprime o valor 1 (nesse caso são os jogadores) e depois o valor 2 que nesse caso é o valor do dado
