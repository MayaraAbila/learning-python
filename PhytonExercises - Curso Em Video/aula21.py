#            INTERACTIVE HELP
#     - ajuda interativa(função, metodo)


"""
print(input.__doc__)
help(input)
"""


#               DOCSTRINGS
# -  documentação do help é uma docstring

"""
def maior(*nums):  # desempacotamento
    """
# > Verifica qual o maior número recibo
#:param nums: numeros recebidos na chamada da função
# Criada por Mayara Abila
"""
    m = 0
    for v in nums:
        if v > m:
            m = v
    print('--'*20)
    print(
        f'Foram informados {len(nums)} números ao todo e o maior valor foi o {m}.')
    print('--'*20)


help(maior)
"""

#             PARAMETROS OPCIONAIS

"""
def somar(a=0, b=0, c=0):  # parametro opcional. Se c nao receber nenhum valor, ele será 0
    s = a + b + c
    print(s)


somar(1, 2, 3)
somar(3, 5)
somar()
"""


#                ESCOPO DE VARIAVEL
#  - local onde a variavel vai existir e onde ela vai deixar de existir
#  - escopo/variavel global: mesmo com a variavel fora da funcao, conseguimos utliza-la porque foi declarada fora da funcao
#  - variavel local: declarada dentro da funcao

# passagem de paramentro, passagem de um valor.


"""
def teste(b):
    global a  # nao crie uma variavel a, use-a como variavel global, entao nesse caso, fora passará a valor 8 
    a = 8  # definicao de outra variavel a, mas nesse caso, local
    b += 4
    c = 2
    print(f'a variável -A- dentro vale {a}, como uma variável local')
    print(f'a variável -B- dentro vale {b}')
    print(f'a variável -C- dentro vale {c}')


a = 5
teste(a)
print(f'a variável -A- fora vale {a}, como global')
# print(f'a variável -A- fora vale {b}') ERRO por falta de escopo
# print(f'a variável -A- fora vale {c}')
"""


#              RETORNANDO VALORES (return)
"""
def somar(a=0, b=0, c=0):
    s = a+b+c
    return s


r1 = somar(1, 5, 20)
r2 = somar(5, 9)
r3 = somar(3)

print(f'Os resultados foram {r1}, {r2} e {r3}.')
"""


"""
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):  # if verdadeiro, subentendido no resultado booleano da função
    print('é par')
else:
    print('É impar')
"""
