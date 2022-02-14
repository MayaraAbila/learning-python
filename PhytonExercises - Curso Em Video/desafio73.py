campeonato = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense',
              'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo',
              'Athletico-PF', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print(f'5 primeiros colocados: {campeonato[:5]}')
print(f'4 últimos colocados: {campeonato[-4:]}') #até o final
print(sorted(campeonato))
print(f'o Chapecoense está na {campeonato.index("Chapecoense")+1}ª posição.') #interpolação
