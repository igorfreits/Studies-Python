km = float(input('Quantos quilômetros você percorreu com o carro alugado? '))
dias = int(input('Quantos dias você passou com o carro alugado? '))
valor = (dias * 60) + (km * 0.15)
print('O preço total é de R${:.2f}'.format(valor))