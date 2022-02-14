dist = float(input('Digite a distância da sua viagem em km: '))
print('Quilometragem total: {}km.'.format(dist))

#preço = dist * 0.50 if dist <= 200 else dist * 0.45

if dist <= 200:
    print('O preço da sua passagem é de R${:.2f} reais'.format(dist*0.5))
else:
    print('O preço da sua passagem é de R${:.2f} reais'.format(dist*0.45))
