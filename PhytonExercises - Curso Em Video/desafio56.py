from time import sleep

velho = 0
mulhernova = 0
somaidade = 0
nome1 = 'nenhum'

for p in range(1, 5):
    nome = str(input(f'Digite o nome da {p}ª pessoa: '))
    idade = int(input(f'Digite a idade da {p}ª pessoa: '))
    sexo = str(input(f'Digite o sexo (F ou M) da {p}ª pessoa: ')).upper()
    print('\n')
    somaidade += idade #soma de todas as idades

    if p == 1 and sexo == 'M':
        velho = idade #o parametro sera a primeira declaração
    else:
        if velho < idade and sexo == 'M': #se houver valores maiores, o valor mudará
            velho = idade
            nome1 = nome

    if sexo == 'F' and idade < 20:
        mulhernova += 1 #se for mulher com menos de 20 anos há uma contagem

sleep(1)
print(f'\nO homem mais velho tem {velho} anos e seu nome é {nome1}.')
print(f'Existem {mulhernova} mulheres com menos de 20 anos.')
print(f'A média das idades do grupo é de: {somaidade/4}')

