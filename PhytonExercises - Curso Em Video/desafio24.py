cidade = input(str('Digite o nome da cidade: ')).strip() #removendo os espaços

cidade = cidade.lower()
cidade = cidade.split()
#print(cidade[0])
#print(cidade[1])

if cidade[0].find('santo') < 0:
    print('A cidade informada não começa com a palavra Santo.')
else:
    print('A cidade informada começa com a palavra Santo.')
