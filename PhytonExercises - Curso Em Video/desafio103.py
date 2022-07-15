def ficha(nome='<desconhecido>', gols=0):
    if nome == '':
        nome = "<desconhecido>"
    if gols == '' or gols.isnumeric() != True:
        gols = 0
    print(f"O jogador {nome} fez {gols} gols(s) no campeonato.")


nome = str(input("Nome do Jogador: "))
gols = str(input("Número de gols: "))
ficha(nome, gols)
