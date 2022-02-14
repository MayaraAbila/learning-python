from calendar import isleap

ano = int(input('Digite um ano: '))

if isleap(ano): #utilizando metodo
    print('O ano digitado é bissexto.')
else:
    print('O ano digitado não é bissexto')

if (ano % 4 & ano % 400 == 0): #utilização matemática
    print('O ano é bissexto')
else:
    print('O ano não é bissexto.')

