# 35 anos de contribuição
from datetime import datetime

cadastro = {}
yearnow = datetime.now().year

cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
idade = yearnow - nasc
cadastro['Idade'] = idade
cadastro['ctps'] = int(input('Carteira de Trabalho (0 para não tem): '))

if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = int(input('Salário: '))
    anosctps = yearnow - cadastro['contratacao']
    if anosctps < 35:
        faltarAposentadoria = 35 - anosctps
        cadastro['aposentadoria'] = cadastro['Idade'] + faltarAposentadoria
        print('--' * 20)
        for k, v in cadastro.items():
            print(f'{k} tem o valor {v}')
    else:
        print('--'*20)
        print('Já aposentado(a)')
else:
    print('--' * 20)
    for k, v in cadastro.items():
        print(f'- {k} tem o valor {v}')
