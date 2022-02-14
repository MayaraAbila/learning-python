from math import sin, tan, cos, radians

angulo = int(input('Qual o valor do ângulo a ser consultado? '))

#as funções estarao em radianos
print('O seno tem o valor de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}'.format(sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))



