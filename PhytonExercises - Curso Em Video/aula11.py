#\033[0; 33; 44m

#todos os códigos em ansi vao ser nesse padrão
#style;text;back

#STYLE - 0, 1, 4, 7
#0 - none
#1 - bold
#4 - underline
#7 - negative

#TEXT - 30 a 37, variando as cores

#BACK - 40 a 17, variando as cores, mesmo conf do text

print('\033[7;30mOlá Mundo!\033[m') #colocar a formatação e finalizar ao final da frase
nome = 'Mayara'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30'}

print('Olá, prazer em te conhecer {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))


