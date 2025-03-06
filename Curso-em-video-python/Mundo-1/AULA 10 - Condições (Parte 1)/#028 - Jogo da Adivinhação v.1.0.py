from random import randint
from time import sleep
computador = randint(0, 5)  # Faz computador "PENSAR"
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))  # Jogador tenta adivinhar
print('-=-' * 20)
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabens! Você conseguiu vencer!')
else:
    print('GANHEI! Eu pensei no numero {} e nao no numero {}!' .format(
        computador, jogador))
