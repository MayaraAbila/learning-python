from random import randint
# 6 numeros = 1 jogo
jogo = []
quant = int(input('Quantos jogos você quer gerar? '))
print()
print(f'Sorteando {quant} jogos.')
print()
for c in range(0, quant):
    for v in range(0, 6):
        num = randint(1, 60)
        if num in jogo:
            num = randint(1, 60)
        jogo.append(num)
    print(f'Jogo {c+1}: {jogo}')
    jogo.clear()
