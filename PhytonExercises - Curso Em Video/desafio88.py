from random import randint
#6 numeros = 1 jogo
quantin = 0
quant = int(input('Quantos jogos você quer gerar? '))
print(f'Sorteando {quant} jogos.')
jogo = []

while quantin <= quant:
    for c in range(0, 6):
        jogo.append(randint(1, 60))
    jogo.clear()
print(jogo)
