palavra = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
           'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for c in palavra:
    print(f'\nNa palavra \033[34m{c.upper()}\033[m temos: ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
