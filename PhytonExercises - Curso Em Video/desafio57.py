sexo = str(input('Digite o seu sexo F/M: ')).upper()

while sexo not in 'MF':
    print('Digite um valor válido!\n').upper()
    sexo = str(input('Digite o seu sexo F/M: '))

print('O valor digitado é válido!')


