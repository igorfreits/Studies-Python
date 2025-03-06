temporaios = []
principal = []
maior = menor = 0

while True:
    temporaios.append(str(input('Digite seu nome: ')))
    temporaios.append(float(input('Digite seu peso: ')))
    if len(principal) == 0:
        maior = menor = temporaios[1]
    else:
        if temporaios[1] > maior:
            maior = temporaios[1]
        if temporaios[1] < menor:
            menor = temporaios[1]

    principal.append(temporaios[:])
    temporaios.clear()

    option = input('Deseja continuar? [s/n]').upper()

    if option in 'N':
        break

print('-=' * 30)
print(f'Ao todo temos {len(principal)} pessoas cadastradas.')

print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}', end='')

print()

print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]}', end='')
