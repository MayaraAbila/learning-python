classe = []
aluno = []
cont = 's'
while cont == 's':
    aluno.append(str(input('Nome: ')))
    for nota in range(1, 3):
        aluno.append(float(input(f'Nota {nota}: ')))
    classe.append(aluno[:])
    aluno.clear()
    cont = str(input('Quer continuar [S/N]? '))
print(classe)

for pessoa in classe:
    print(f'{pessoa[0]} teve a média {(pessoa[1] + pessoa[2])/2}.')

while True:
    mostrar = input('Mostrar notas de qual aluno [999 para parar]? ')
    if mostrar == '999':
        break
    for pessoa in classe:
        if mostrar == pessoa[0]:
            print(f'{pessoa[1]} e {pessoa[2]}')
print()
print('Programa Finalizado')
