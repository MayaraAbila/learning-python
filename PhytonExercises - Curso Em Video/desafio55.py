maior = 0
menor = 0

for pes in range(1, 6):
    peso = float(input(f'Peso da {pes}ª pessoa: '))
    if pes == 1: #o primeiro valor será usado como comparação
        maior = peso
        menor = peso
    else:
        if peso > maior: #se os próximos laços forem maiores, serão substituidos
            maior = peso
        if peso < menor: #assim como os menores
            menor = peso

print(f'O peso maior é {maior} e o menor é {menor}')