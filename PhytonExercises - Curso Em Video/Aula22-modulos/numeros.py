#           MODULARIZACAO
# surgiu na decada de 60 com o avanco do tamanho dos sistemas. Dividir o programa em pequeno modulos, aumentando a legibilidade e a manutenção
# import uteis  # utilizar dessa forma para nao causa incompatibilidade de importação
from uteis import numeros


num = int(input("Digite um valor: "))
print(
    f'O fatorial de {num} é {numeros.fatorial(num)}. O dobro é {numeros.dobro(num)} e o triplo {numeros.triplo(num)}')


#             PACOTES (OUTRAS LINGUAGENS CHAMAM DE BIBLIOTECA)
# pasta que contem modulos separados por assunto (por ex, tratamento de numeros, strings, cores, datas)
