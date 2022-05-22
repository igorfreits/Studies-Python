velocidade  = float(input('Qual é a sua velocidade atual?'))
if velocidade > 80:
    print('MULTADO! Você exceu o limite de velocidade que é 90km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R$ {:.2f}!' .format(multa))
print('Tenha um bom dia! Dirija com segurança')