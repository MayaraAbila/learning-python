salario = float(input('Digite o valor do salário: '))

if (salario > 1250):
    print('O seu salário terá um aumento de 10%, sendo: R${:.2f}'.format(salario*0.10))
else:
    print('O seu salario terá um aumento de 15%, sendo R${:.2f}'.format(salario*0.15))
