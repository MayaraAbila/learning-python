primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
amais = 10

while amais != 0:
    total = total + amais
    while cont <= total:
        print(f'{termo}', end=' > ')
        termo += razão
        cont += 1
    print('PAUSA')
    amais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
