vel = float(input('Digite a velocidade do carro: '))

if vel > 80:
    multa = float((vel - 80)*7)
    print('Você esta acima do limite de velocidade e irá pagar uma multa no valor de R${:.2f} reais.'.format(multa))
else:
    print('Você esta dentro do limite de velocidade!')
