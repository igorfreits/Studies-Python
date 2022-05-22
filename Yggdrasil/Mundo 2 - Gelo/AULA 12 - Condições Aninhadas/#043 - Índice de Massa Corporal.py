peso = float(input('Qual o seu peso?(KG) '))
altura = float(input('Qual  sua altura?(m) '))

imc = peso / (altura ** 2)

print(f'O iMC dessa pessoa e de {imc:.1f}')
if imc < 18.5:
    print('Voce esta ABAIXO do peso normal')
elif 18.5 <= imc <25:
    print('PARABENS, voce esta na faixa de peso NORMAL')
elif 25 <= imc < 30:
    print('Voce esta em SoBREPESO')
elif 30 <= imc < 40:
    print('Voce esta em OBESIDADE, CUIDADO')
elif imc >= 40:
    print('Voce esta em obesidade MÓRBIDA, CUIDADO')

