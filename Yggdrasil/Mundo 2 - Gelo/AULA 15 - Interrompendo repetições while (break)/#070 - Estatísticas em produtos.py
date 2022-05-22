print('-'*30)
print('Kwik-E-Mart')
print('-'*30)

preçototal = 0
valormax = ''
milzao =

while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('preço R$: '))

    preçototal += preço

    if preço > 1000:
        valormax = produto

    compra = ' '
    while compra not in 'SN':
        compra = str(input('Deseja continuar? [S/N]: ')).strip()[0].upper()

    if compra == 'N':
        break

print('-'*30)
print('Fim do programa')
print('-'*30)

print(f'O valor da sua compra deu {preço:.2f} R$')
print(f'')
