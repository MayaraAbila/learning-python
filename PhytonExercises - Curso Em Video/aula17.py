print('LISTAS são colocadas entre colchetes:\033[1;31m []\033[0;0m e podem ser modificadas.')

lanche = ['hamburguer', 'suco', 'pizza', 'picole', 'cookie']
print(f'\n{lanche}')
lanche[3] = 'milk-shake' #SUBSTITUIR
print(lanche)
lanche.append('bala') #ADICIONAR elemento ao final
print(lanche)
lanche.insert(0, 'cachorro-quente') #INSERIR um elemento na POSIÇÃO 0
print(lanche)
del lanche[3] #ELIMINAR o elemento na posição 3
#lanche.pop(3) #normalmente utilizado para eliminar o ultimo elemento, mas pode ser usado dessa forma, inserindo o paramento desejado
#lanche.remove('pizza') #indicar o valor que quer eliminar e não a posição, se houver repetição, ele so vai remover o primeiro
valores = list(range(4, 11))
print(valores)
#valores.sort(reverse=True) #organizar de forma decrescente
print(valores.sort())
for c, v in enumerate(valores): #o ENUMERATE vai pegar sempre a chave/indice e o valor
    print(f'{v} na posição {c}')

números = list()
for cont in range(0, 5):
    números.append(int(input('Digite um valor: '))) #começar com a LISTA VAZIA e ADICIONAR elemento conforme input
print(números)

print('\n\033[1;31mAs listas em python são interligadas e a partir do momento que igualo as duas e altero algum elemento, isso é alterado nas duas.'
      '\nPara fazer uma cópia é necessário: "B = A[:]"\033[0;0m')
