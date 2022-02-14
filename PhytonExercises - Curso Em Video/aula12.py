#estrutura condicional aninhada - condicionais dentro de outras
nome = str(input('Qual o seu nome? '))
if nome == 'Mayara':
    print('Que nome bonito {}!'.format(nome))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem comum no Brasil!')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
