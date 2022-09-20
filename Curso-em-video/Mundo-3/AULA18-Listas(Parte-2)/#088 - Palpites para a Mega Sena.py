from random import randint
from time import sleep

lista = list()
jogos = list()
print('-='*3, 'JOGA NA MEGA SENA', '-='*3)

quant = int(input('Quantos jogos você quer que eu sorteie? '))

tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print(f'SORTEANDO {quant} JOGOS...')

for i, l in enumerate(jogos):
    print(f'{i+1}º JOGO: {l}')
    sleep(1)
