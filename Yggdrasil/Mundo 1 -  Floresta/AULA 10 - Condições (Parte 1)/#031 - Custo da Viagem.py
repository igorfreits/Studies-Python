viagem = float(input('Quantos km tem sua viagem? '))
print(('Sua viagem sera de {} km' .format(viagem)))
if viagem <=200:
    preço = viagem * 0.50
else:
    preço = viagem  * 0.45
print('E o preço da sua passagem ser de R$ {:.2f}'.format(preço))