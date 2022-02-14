n1 = float(input('Digite o primeiro comp de reta: '))
n2 = float(input('Digite o segundo comp de reta: '))
n3 = float(input('Digite o terceiro comp de reta: '))

if ((n1 + n2 > n3) and (n2 + n3 > n1) and (n3 + n1 > n2)):
    if n1 == n2 == n3:
        print('Esse triangulo será equilátero')
        #todos os lados iguais
    elif n1 == n2 or n2 == n3 or n3 == n1:
        print('Esse triangulo é Isósceles')
        #dois lados iguais
    elif n1 != n2 != n3 != n1:
        print('Esse triangulo é escaleno')
        #todos os lados diferentes
else:
    print('Esses comprimentos não podem formar um triangulo!')
    #indentação importante para identificar as condições

# desigualdade triangular: a soma de dois lados deve ser sempre maior ao terceiro.

