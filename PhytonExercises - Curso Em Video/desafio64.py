num = cont = soma = 0
num = int(input('Digite um número: '))

while num != 999: #flag
    cont += 1
    soma += num
    num = int(input('Digite um número: ')) #inverter a ordem da pergunta para iniciar na contagem e na soma, caso seja igual a 999, ele n repete o laço
print(f'A quant de nº digitados foi {cont} e a soma entre eles é {soma}.')
