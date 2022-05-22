print('Gerador de PA')
primeiro = int(input('Primeiro Termo: '))
razão = int(input('razão da PA: '))

termo = primeiro
contador = 1

while contador <= 10:
    print(f'{termo} > ', end=' ')
    termo += razão
    contador += 1
print('FIM')
