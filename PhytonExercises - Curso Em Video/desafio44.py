preço = float(input('Qual o valor do produto? '))
pgto = int(input('FORMAS DE PAGAMENTO \n'
                 '1 - Dinheiro/Cheque; \n'
                 '2 - A vista Cartão; \n'
                 '3 - Em até 2x cartão; \n'
                 '4 - 3x ou mais no cartão: \n'
                 'Qual a sua opção? '))

if pgto < 1 and pgto > 4:
    print('Escolha um número válido')
elif pgto == 1:
    print(f'Valor a pagar: R${preço-(preço*0.1):.2f}')
elif pgto == 2:
    print(f'Valor a pagar: R${preço-(preço*0.05):.2f}')
elif pgto == 3:
    print(f'Valor a pagar: R${preço:.2f}')
else:
    print(f'Valor a pagar: R${preço+(preço*0.2):.2f}')
