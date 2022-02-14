#while - estrutura de repetição com teste lógico (quando não ha parametros a serem contados)
#for - estrutura de repetição com variável de controle #somente quando sei o limite

#---------------1-----------------

#for c in range(1, 10):
#    print(c)
#print('Fim')

#c = 1
#while c < 10:
#    print(c)
#    c += 1
#print('Fim')

#----------------2------------------

#n = 1
#while n != 0: #condição de parada
#    n =int(input('Digite um número: '))
#print('Fim')

#---------------3-------------------

#r = 'S'
#while r == 'S':
#    n = int(input('Digite um valor: '))
#    r = str(input('Quer continuar [S/N]: ')).upper()
#print('Fim')

#--------------4----------------

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Foram lidos {par} números pares e {impar} números ímpares')
