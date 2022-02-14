totmaior = 0
totmenor = 0

for c in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    #print(ano)
    idade = 2021 - ano
    if idade >= 21:
        totmaior += 1
        #print('Atingiram a maioridade')
    else:
        totmenor += 1
        #print('Ainda não atingiram:')

print(f'São {totmaior} maiores e {totmenor} menores.')
