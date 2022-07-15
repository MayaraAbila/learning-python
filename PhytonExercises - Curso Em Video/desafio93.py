jogador = {}
gols = []
tot = 0

jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for c in range(0, partidas):
    gols.append(int(input(f"  Quantos gols na partida {c+1}? ")))
    jogador['gols'] = gols

jogador['total de gols'] = sum(gols)  # soma de valores

print('--'*20)
for k, v in jogador.items():
    print(f'{k} tem o valor {v}')
print('--'*20)

print(f"O jogador {jogador['nome']} jogou {partidas} partidas")
for i, v in enumerate(gols):
    print(f"Na partida {i+1} o total de gol(s) foi de {v}")
