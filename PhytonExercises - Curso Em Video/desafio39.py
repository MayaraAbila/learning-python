from datetime import date
atual = date.today().year

nasc = int(input('Qual é o seu ano de nascimento? '))

idade = atual - nasc

if idade == 18:
    print('Este ano você deve se alistar para o serviço militar.')
elif idade > 18:
    tempo = idade - 18
    print(f'Já passou {tempo} anos do ano obrigatório de alistamento.')
else:
    tempo = 18 - idade
    print(f'Ainda faltam {tempo} anos para você se alistar.')
