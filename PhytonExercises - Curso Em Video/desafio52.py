num = int(input('Digite um número: '))
tot = 0 #contador para o número de divisões

for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')

if tot == 2: #como o número primo só deve dividir duas vezes, o contador deve ser 2
    print('\nO número digitado é primo')
else:
    print('\nO número digitado não é primo')
#pq ele ta puxando a cor se ela ta dentro do laço?