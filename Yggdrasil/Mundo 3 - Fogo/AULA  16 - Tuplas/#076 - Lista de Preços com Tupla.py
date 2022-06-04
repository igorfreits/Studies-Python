products = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print(f'{"Listagem de  produtos":-^39}')

for c in range(0, len(products)):
    if c % 2 == 0:
        print(f'{products[c]:.<30}', end='')
    elif c % 2 == 1:
        print(f'R${products[c]:>7.2f}')

print('-'*39)
