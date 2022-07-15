import pandas as pd
jogador = {}  # dicionário
time = []  # lista
gols = []  # lista
tot = partidas = 0

while True:
    jogador['Nome'] = str(input('Nome do Jogador: '))
    partidas = int(
        input(f"Quantas partidas {jogador['Nome']} jogou? "))
    for n in range(0, partidas):
        gol = int(input(f"  Quantos gols na partida {n+1}? "))
        gols.append(gol)
        tot = tot + gol
        jogador['Placares'] = gols
        jogador['QuantGols'] = tot
    time.append(jogador.copy())
    gols = []
    tot = 0
    continuar = str(input('Quer continuar? [S/N] ')).lower()[0]
    print('--'*20)
    if continuar == 'n':
        break

df = pd.DataFrame(time, columns=['Nome', 'Placares', 'QuantGols'])
print(df)

print(len(time))

while True:
    busca = int(
        input('Mostrar dados de qual jogador [999 para para o programa]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe o jogador com código {busca}')
    else:
        print(
            f'O jogador {time[busca]["Nome"]}, fez {time[busca]["Placares"]} gols em cada partida, totalizando {time[busca]["QuantGols"]} gols.')
    print('--'*20)
