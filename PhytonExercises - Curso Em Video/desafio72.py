extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20: '))

while num < 0 or num > 20:
    num = int(input('Número inválido. Digite um número que esteja entre 0 e 20: '))

pos = num

print(f'Você digitou o número {extenso[pos]}.')
