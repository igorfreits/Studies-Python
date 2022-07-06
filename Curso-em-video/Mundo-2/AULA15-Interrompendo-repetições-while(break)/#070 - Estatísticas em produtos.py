print('-'*30)
print('Kwik-E-Mart')
print('-'*30)

preçototal = thousand = menor = contador = 0
barato = ''

while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('preço R$: '))
    preçototal += preço
    contador += 1

    if preço > 1000:
        thousand += 1

    if contador == 1 or preço < menor:  # Simplificação
        menor = preço
        barato = produto

    compra = ' '
    while compra not in 'SN':
        compra = str(input('Deseja continuar? [S/N]: ')).strip()[0].upper()

    if compra == 'N':
        break


print(f'{"Fim do programa":-^40}')


print(f'O valor da sua compra deu R${preço:.2f}')
print(f'Temos {thousand} produtos acima de R$1000.00 ')
print(f'O produto mais barato custa R${menor:.2f}')
