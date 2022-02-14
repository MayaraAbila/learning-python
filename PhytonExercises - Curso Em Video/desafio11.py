alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))

# area = alt*larg
# tinta = area/2
# 1 litro = 2m2

print('A área da parede é de {:.2f} m2 e serão necessários {:.2f} litros de tinta para pinta-la'.format((alt*larg), ((alt*larg)/2)))