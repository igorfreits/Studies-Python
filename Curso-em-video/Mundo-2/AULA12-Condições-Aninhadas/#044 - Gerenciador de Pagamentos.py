print(f'{" LOJAS COLOMK ":=^40}')

valor = float(input('Qual o valor da compra? R$: '))

print("""FORMA DE PAGAMENTO
[ 1 ] a vista dinheiro/cheque - 10% de desconto
[ 2 ] a vista no cartão - 5% de desconto
[ 3 ] 2x no cartão - preço normal
[ 4 ] 3x no cartao ou mais - 20% de juros""")

pagamento = int(input('Qual opção? '))

if pagamento == 1:
    desconto = valor - (valor * 10 / 100)
    print(
        f'Sua compra de R${valor:.2f} vai custar {desconto:.2f} com 10% de desconto no final')
elif pagamento == 2:
    desconto = valor - (valor * 5 / 100)
    print(
        f'Sua compra de R${valor:.2f} vai custar {desconto:.2f} com 5% de desconto no final')
elif pagamento == 3:
    parcela = valor / 2
    print(f'Sua compra sera parcela em 2x de {parcela:.2f}')
    print(
        f'Sua compra de R${valor:.2f} vai custar {valor:.2f} sem desconto no final')
elif pagamento == 4:
    parcela = int(input('Quantas parcelas? '))
    juros = valor + (valor * 20 / 100)
    total_parcelas = juros / parcela
    print(
        f'Sua compra sera parcelada em {parcela}x de {total_parcelas:.2f} e terá um total de {juros:.2f} no final')
else:
    print('OPÇÃO INVALIDA, ESCOLHA UMA FORMA DE PAGAMENTO!')
