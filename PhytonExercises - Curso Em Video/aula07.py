nome = str(input('qual o seu nome? '))
print('Prazer em te conhecer, {:20}!'.format(nome))

# :20 - escrever em 20 espaços
# :>20 - alinhamento e o nome aparecer no final | < aparecer no começo
# :=^20 - aparecer no meio de vinte sinais de igual
# :^20 - centralizado em 20 espaços

n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2 #divisão inteira
e = n1 ** n2 #potência
print('A soma vale {}, \n o produto {} e a \n divisão {:.2f}'.format(s, m, d), end=' ') # 2 casas flutuantes; ao final da linha, não quebrar a linha
print('Divisão inteira {} e potência {}'.format(di, e))

