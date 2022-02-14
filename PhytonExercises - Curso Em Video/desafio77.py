palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'praticar', 'trabalhar', 'mercado'
            'futuro', 'programador')

for p in palavras:
    print(f'\nNa palavra {p.upper()}, temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
            