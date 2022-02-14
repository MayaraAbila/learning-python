valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salario? '))
anos = int(input('Em quantos anos você vai pagar a casa? '))

valor_prestação = (valor_casa/anos)/12 #dividi primeiro o valor pago em anos para deps dividir por mês
#print(valor_prestação)

limite = salario*0.3

if valor_prestação > limite:
    print('O empréstimo não pode ser realizado porque ultrapassa 30% da sua renda!')
else:
    print('Você poderá realizar o empréstimo e pagará parcelas de R${:.2f}'.format(valor_prestação))