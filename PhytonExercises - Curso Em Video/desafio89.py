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
    # ele só vai fazer o laço ate o tamanho que for a classe, por isso ele faz duas vezes e para.
    mostrar = str(input('Mostrar notas de qual aluno [999 para parar]? '))
    for pessoa in classe:
        print(mostrar)
        if mostrar == pessoa[0]:
            print(f'{pessoa[1]} e {pessoa[2]}')
        if mostrar == '999':
            break
        mostrar = ''
