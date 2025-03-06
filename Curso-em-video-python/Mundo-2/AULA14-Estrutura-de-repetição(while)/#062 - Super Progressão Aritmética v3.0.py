print('Gerador de PA')
primeiro = int(input('Primeiro Termo: '))
razão = int(input('razão da PA: '))

termo = primeiro
contador = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo} > ', end=' ')
        termo += razão
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))

print(f'Progressão finalizada com {total} termos mostrados')
