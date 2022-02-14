n1 = float(input('Digite o primeiro comp de reta: '))
n2 = float(input('Digite o segundo comp de reta: '))
n3 = float(input('Digite o terceiro comp de reta: '))

if ((n1 + n2 > n3) and (n2 + n3 > n1) and (n3 + n1 > n2)):
    print('Essas retas podem formar um triangulo!')
else:
    print('Essas retas NÃO podem formar um triangulo!')

# desigualdade triangular: a soma de dois lados deve ser sempre maior ao terceiro.

