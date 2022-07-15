#                ERROS E EXCEÇÕES

# erros de exceção - sintaxe esta ok mas ha algum erro relacionado as regras de funcionamento do códiagonal
# pythonexceptions list


# tratamento de erro
try:
    # operacao para tentar
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
# except Exception as erro:
    # se der problema
    # print(f'Erro: {erro.__class__}') #imprima o erro na tela
# except (TypeError, ValueError):
#    print('Tivemos um problema com os tipos de dados de você digitou.')
# except ZeroDivisionError:
#    print('Não é possível dividir um número por zero.')
# except KeyboardInterrupt:
#    print('O usuário preferiu não informar os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    # se der certo
    print(f'O resultado é: {r:.1f}')
finally:
    # vai acontecer independente se der erro ou não
    print('Volte sempre!')
