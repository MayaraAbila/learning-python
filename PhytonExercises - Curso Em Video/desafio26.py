frase = input(str('Digite uma frase: ')).strip().lower()

print('O caractere "A" aparece {} vezes na frase'. format(frase.count('a')))
print('A primeira letra "A" se inicia na posição {}.'. format(frase.find('a')))
print('A ultima letra "A" esta na posição {}.'.format(frase.rfind('a'))) #procurar do lado direito


