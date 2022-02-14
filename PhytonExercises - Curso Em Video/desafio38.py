num1 = int(input('Escolha o primeiro número: '))
num2 = int(input('Escolha o segundo número: '))

if num2 > num1:
    print('O segundo número escolhido é o maior porque é o número {}'.format(num2))
elif num1 > num2:
    print('O primeiro número escolhido é o maior')
else:
    print('Não existe valor maior, os dois números são iguais')
