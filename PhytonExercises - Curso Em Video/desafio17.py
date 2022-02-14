from math import hypot

cat1 = float(input('Digite o comprimento do cateto oposto: '))
cat2 = float(input('Digite o comprimento do cateto adjacente: '))

print('O comprimento da hipotenusa é de {:.2f}'.format(hypot(cat1, cat2)))


