n = 1
mult = 1

while True:
    n = int(input('\033[0;0mQual tabuada você deseja visualizar? '))
    if n < 0:
        break


    #while mult <= 10:
    #    print(f'\033[1;92m{n} x {mult} = {n*mult}')
    #    mult += 1
    #mult = 1 #retornar a tabuada pois no laço anterior a variavel de multiplicação ja estava igual a 10$

    #soluçaõ com for, como intervalo limitado, nao teria que retornar a variavel mult para 1
    for c in range(1, 11):
        print(f'\033[1;92m{n} x {c} = {n * c}')


    print('\033[0;0m-'*32)
print('\n\033[1;31mPrograma de Tabuada Encerrado')
