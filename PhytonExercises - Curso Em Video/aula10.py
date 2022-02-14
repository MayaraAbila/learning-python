#carro.siga() - o carro é o objeto e o siga é o metodo e como metodo, tem o parenteses no final
#estrutura sequencial # estrutura condicional

# if blocl verdadeiro: else: bloco falso

# CONDIÇÃO SIMPLIFICADA PYTHON
# print('carro novo' if tempo <= 3 else 'carro velho') print('fim')

"""
nome = str(input('Qual é o seu nome? '))
if nome == 'Mayara':
    print('Seu nome é tão bonito!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2

print('A sua média foi {:.1f}.'.format(m))

if m >= 6.0:
    print('Essa é uma boa nota, Parabéns.')
else:
    print('Essa não é uma boa nota.')
