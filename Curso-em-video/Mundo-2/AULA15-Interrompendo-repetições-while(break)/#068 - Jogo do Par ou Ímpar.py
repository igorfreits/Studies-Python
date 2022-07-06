from random import randint

v = 0
while True:
    jogador = int(input('Digite um numero: '))
    computador = randint(0, 10)
    tipo = ' '
    total = jogador + computador
    while tipo not in 'PI':
        tipo = str(input('PAR OU IMPAR [P/I]: ')).strip().upper()[0]
    print(
        f'Voce jogou {jogador} e o computador {computador} totalizando {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU')
            v += 1
        else:
            print('Voce PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU')
            v += 1
        else:
            print('Voce PERDEU')
            break
    print('Vamos jogar novamente')
print(f'GAME OVER! Voce venceu {v} vezes')
