#cadeia de caracteres/string - frase ou palavra.
#em pyhton sempre estara entre aspas simples ou dupla

#a string, declarada em uma variável esta dentro de uma espaço da mesmoria mas será
#dividida em mini espaços que serão os indices, posição de cada caractere, incluindo o espaço

frase = 'Curso em Video Python'

# FATIAMENTO
#frase(9) - retornará o caractere que esta na posição 9
# 9:13 retornará os caracteres que estão em 9 até o 12, pois exclui o ultimo caractere
# 9:21:2 vai pegar do 9 ao 20, pulando de 2 em 2
# :5 - vai pegar do inicio até o 4
# 15: - vai iniciar no 15 até o final, considerando o ultimo indice
# 9::3 - vai começar no 9, ir até o final e ir pulando de 3 em 3

# - ANALISES DE STRING

# len(frase) - comprimento da frase/lenght
# frase.count('o') - contar quantas vezes aparece a letra o
# frase.count('o', 0, 13) - ira contar quantos ós aparecem entre 0 e 12(fatiamento com contagem)
# frase.find('deo') - vai procurar a posição que inicia essa sequencia de caracteres
# frase.find('android') - retornara o valor -1 indicando que a string nao existe na string analisada
# 'Curso' in frase - existe a palavara curso em frase? retornará true

# TRANSFORMAÇÃO

# frase.replace('Python', 'Android') - vai substituir na frase o conjunto de caracteres 'python' por 'android'
# frase.upper() - transformará as letras em maiusculas
# frase.lower() - transformará as letras em minusculas
# frase.capitalize() - deixará somente o primeiro caractere em maiuscula
# frase.title() - transformará todas as primeiras letras de palavras em maiusculas, considerando a quebra no espaço
# frase.strip() - removerá todos os espaços inuteis da frase
# frase.rstrip() - r de right (direita), removerá somente os ultimos espaços
# frase.lstrip() - left, ira remover somente os espaços da esquerda

# DIVISÃO

# frase.split - vai dividir as palavras dentro daquela cadeia de caracteres, reconsiderando suas posições
# curso em video iniciará no 0 e termina no 4, sendo o 0 da lista que foi criada a partir do slipt, agora com 0,1,2,3

# JUNÇÃO

# '-'.join(frase) - irá juntar os pedaços anteriores separados, novamente em uma unica cadeia de strings utlizando o traço para separa-las

print(frase[::2])
print(frase.upper().count('O'))
print(len(frase))
frase.strip()
print(len(frase))

print(len(frase.strip())) #é necessário colocar o strip para fazer a contagem dessa forma pq ele nao vai guardar o que foi feito anteriormente, ja que é uma transformação momentanea e nao estamos alterando a variavel em sua raiz

print(frase.replace('Python', 'Android'))

print('Curso' in frase) #letra maiuscula e minusculas são diferenciadas
print(frase.find('Video'))

dividido = frase.split()
print(dividido[0])
print(dividido[3][2]) #dentro do objeto na posição 3, me mostre qual a letra que esta na posição 2
