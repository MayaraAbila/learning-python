tot18 = homens = mulheres = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).lower()
    if idade >= 18:
        tot18 += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f':
        if idade < 20:
            mulheres += 1
    continuar = str(input('Você quer continuar [S/N]? ')).lower()
    if continuar == 'n':
        break
print(f'{tot18} pessoas tem mais de 18 anos.'
      f'\n{homens} homens foram cadastrados.'
      f'\n{mulheres} mulheres tem menos de 20 anos.')
