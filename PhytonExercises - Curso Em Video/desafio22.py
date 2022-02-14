nome = str(input('Qual o seu nome completo: '))

print('Seu nome em letras maiusculas fica: {}'.format(nome.upper()))
print('Seu nome em letras maiusculas fica: {}'.format(nome.lower()))

print('O número de caracteres no seu nome, sem considerar os espaços é: {}'.format(len(nome.replace(" ", "")))) #substitui os espaços para 'sem espaço' e fiz a contagem dos caracteres
print(len(nome) - nome.count(' '))
#Outra forma de fazer é ler o tamanho da string e subtrair os espaços que houver

nome = nome.split()

print('O seu primeiro nome é {} e ele tem {} letras.'.format(nome[0], len(nome[0])))
print(nome.find(' '))
#outra forma de fazer: buscar a posição do primeiro espaço, e como se incia em 0, será a quant de caracteres.
#opiniao: não é a melhor forma de fazer porque ele estará puxando a posição e não necessariamente a quant, por mais que sejam iguais.
