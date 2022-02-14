#iteração, laços, repetições

#LAÇO COM VARIÁVEL DE CONTROLE

for c in range(0, 6): #vai printar somente 5 vezes pois no ultimo ele para
    print(c)
print('fim') #necessário deixar fora do for para entender que nao faz parte da repetição - indentação

for c in range(9, 0, -1): # o ultimo eu to falando qual é a iteração, nesse caso pulando dois. -1: contar de tras pra frente
    print(c)
print('fim')
#quando é ao contrário ele nao vai considerar o ultimo que nesse caso é o 0

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('fim')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n #s = s + n
print(f'A somatória de todos os valores foi {s}')
