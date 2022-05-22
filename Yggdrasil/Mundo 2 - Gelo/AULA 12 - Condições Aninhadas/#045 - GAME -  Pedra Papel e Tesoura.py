import time
from random import randint

itens = ('PEDRA', 'PAPEL', 'TESOURA')
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")

jogadar = int(input('Qual a sua opção? '))
computador = randint(0, 2)

time.sleep(0.5)
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(1)
print('PO')

print('=-' * 20)
print(f'computador escolheu: {(itens[computador])}')
print(f'Jogador escolheu: {(itens[jogadar])}')
print('=-' * 20)

if computador == 0:  # Computador jogou PEDRA
    if jogadar == 0:
        print('EMPATE!')
    elif jogadar == 1:
        print('O jogar ganhou!')
    elif jogadar == 2:
        print('O computador ganhou!')

elif computador == 1:  # Computador jogou PAPEL
    if jogadar == 0:
        print('O computador ganhou!')
    elif jogadar == 1:
        print('EMPATE!')
    elif jogadar == 2:
        print('O jogador ganhou!')

elif computador == 2:  # Computador jogou TESOURA
    if jogadar == 0:
        print('O jogador ganhou!')
    elif jogadar == 1:
        print('O computador ganhou!')
    elif jogadar == 2:
        print('EMPATE!')
