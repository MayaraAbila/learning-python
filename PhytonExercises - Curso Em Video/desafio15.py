km = float(input('Qual a quantidade de KM percorridos? '))
dias = int(input('Quantos dias o carro foi utilizado? '))

print('O preço a pagar pelo carro é de R${:.2f} reais.'.format((km*0.15)+(dias*60)))
