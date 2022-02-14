lista = str(input('Digite uma expressão: ')) #toda string é uma lista
#print(lista[1])
#abrepar = fechapar = 0
#for c in lista:
#    if c == '(':
#        abrepar += 1
#    if c == ')':
#        fechapar += 1
#if abrepar != fechapar:
#    print('Essa expresão está errada!')
#else:
#    print('A expressão está correta!')

if lista.count('(') == lista.count(')'):
    print('A expressão está correta!')
else:
    print('Essa expresão está errada!')
