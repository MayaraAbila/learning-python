numero = int(input('Escolha um número: '))
escolha = str(input('Escolha qual será a base de conversão: \n'
                    '1 - binário; \n'
                    '2 - octal ou \n'
                    '3 - hexadecimal: '))

#função bin() - imprime o nuemro com o seu prefixo 0b
#função format(value,format_spec) - imprime sem o prefixo, formatando a saida
#metodo str.format() -

if escolha == '1':
    print('O número escolhido em número binário é {}'.format(format(numero, "b")))
elif escolha == '2':
    print('O número escolhido em número octal é {}'.format(format(numero, "o")))
else:
    print('O número escolhido em número hexadecimal é {}'.format(format(numero, "x")))
