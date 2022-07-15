pessoa = {}  # dicionario
grupo = []  # lista
tot = totf = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [F/M]: ')).lower()[0]
    # if pessoa['sexo'] == 'f':
    #    totf = totf + 1
    pessoa['idade'] = int(input('Idade: '))
    tot += pessoa['idade']
    grupo.append(pessoa.copy())
    # copio o dicionário criado para dentro da lista. Como as chaves nao se alteram, os valores das mesmas são substituidas e por isso os valores dentro da lista não são duplicados
    continuar = str(input('Quer continuar? '))
    while continuar != 'n' and continuar != 's':
        print("Entrada invalida. Digite apenas 's' ou 'n'")
        continuar = str(input('Quer continuar? '))
    if continuar == 'n':
        break

print('--'*20)
print(f"A) Foram cadastradas {len(grupo)} pessoa(s)")
mediaIdade = tot/len(grupo)
print(f"B) A média de idade foi: {mediaIdade:5.2f}")
# 5 casas ao todo e 2 decimais
#print(f"A quantidade de mulhere(s) cadastrada(s) foi de: {totf} ")
print(f"C) As mulheres cadastradas foram ", end='')

for p in grupo:  # para cada dicionário dentro da lista
    if p['sexo'] == 'f':  # eu vou verificar se a chave sexo é igual a feminino
        print(f'{p["nome"]} ')

print('D) Lista das pessoas que estão acima da média de idade: ')
for p in grupo:
    if p['idade'] > mediaIdade:
        for k, v in p.items():
            print(f"{k} = {v}")
