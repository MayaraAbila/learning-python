class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f'{bcolors.OKCYAN}VARIAVEIS COMPOSTAS: TUPLAS, LISTAS, DICIONÁRIO{bcolors.ENDC}')

print(f'{bcolors.BOLD}Toda variavel simples reserva um unico espaço na memória.'
      '\ntuplas são variaveis compostas e podem armanezar vários valores que são identificados por indices'
      '\n Uma string é uma variavel composta - lista'
      '\n() - tupla'
      '\n[] - lista'
      f'\n chaves - dicionário{bcolors.ENDC}'
      f'\n{bcolors.OKCYAN}CARACTERISTICA DA TUPLA:{bcolors.ENDC}'
      f'\n{bcolors.BOLD}-As tuplas são imutáveis: dentro do python não é possível alterar os valores de dentro de uma variável composta que seja uma tupla.'
      f'\nÉ possível deletar uma tupla de forma inteira: del(pessoa){bcolors.ENDC}')

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
#print(lanche)
#print(lanche[:-1])
#print(len(lanche))

#for comida in lanche:
#    print(f'Eu vou comer {comida}.')

for pos, comida in enumerate(lanche):
   print(f'Eu vou comer {comida} na posição {pos}.')

#for cont in range(0, len(lanche)): #como é um intervalo ele vai printar posições
#    print(f'{lanche[cont]} na posição {cont}.') #printar o lanche na posição cont

#print(sorted(lanche)) #printar em ordem sem alterar a ordem dos elementos

print(f'{bcolors.OKCYAN}-------Junção de tuplas e outras propriedades-------{bcolors.ENDC}')
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #irá juntar as duas tuplas na ordem da operação, tanto que b + a traz uma combinação diferente
print(c)
print(c.count(5)) #contar quantas vezes o cinco aparece na tupla c
print(c.index(8)) #em que posição está o 8
print(c.index(5, 3)) #mostrar a posição do numero 5 a partir da posição 3 - nesse caso vai pegar o segundo e não o primeiro (deslocamento)

print(f'{bcolors.OKCYAN}------Armazenamento de diferentes tipos de variáveis dentro da mesma tupla------{bcolors.ENDC}')
pessoa = ('Mayara', 24, 'F', 64)
print(pessoa)