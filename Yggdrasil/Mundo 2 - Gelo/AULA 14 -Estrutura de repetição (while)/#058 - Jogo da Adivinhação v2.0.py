from random import randint

computador = randint(0, 10)
print('Sou o seu computador...'
      '\n Acabei de pensar em numero de 0 a 10'
      '\n Sera que você consegue adivinhar?')

acertou = False

tentativas = 1
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    tentativas += 1

    if computador == jogador:
        acertou = True

    else:
        if computador < jogador:
            print('Menos...Tente outra vez! ')

        elif computador > jogador:
            print('Mais...Tente outra vez! ')

print(f'Parabens voce acertou com {tentativas} tentativas!')
