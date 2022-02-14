dados = ['Pedro', 25]
pessoas = list()
pessoas.append(dados[:]) #fez uma cópia dos elementos da lista dados, lista dentro de lista
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]] #listas compostas
print(pessoas[0]) # vai a primeira lista inteira
print(pessoas[0][0]) # vai buscar a primeira lista e o primeiro elemento dessa lista

print()

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #primeira copia com os dados originais, gustavo, 40
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) #copiei a lista teste para a galera pela segunda vez, com os dados alterados
print(galera)

print()

galera1 = [['Jao', 10], ['Maria', 15], ['Mayara', 24], ['Jonathan', 26]]
for p in galera1:
    #print(p) #ele vai printar as listas
    #print(p[0]) #somente os nomes de todas as listas
    #print(p[1]) #idades de todas as listas
    print(f'{p[0]} tem {p[1]} anos de idade')

print()

galera2 = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera2.append(dado[:])
    #print(dado)
    dado.clear() #se eu não limpar os valores da lista dado a cada laço, ele vai adicionar os valores que ja foram armazenados, novamente na galera 2
    #já que a cada laço, ele faz uma cópia dos valores digitados e armazenados na lista dado; como essa é uma lista que esta sendo copiada em galera2
    #será uma lista composta
print(galera2)
for p in galera2:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} é menor de idade')
