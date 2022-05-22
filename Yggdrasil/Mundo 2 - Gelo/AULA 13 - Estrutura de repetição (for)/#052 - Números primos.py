n1 = int(input('Digite um numero: '))
total = 0

for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[m O numero {c} foi divido {total}')

if total == 2:
    print('E por isso ele e PRIMO')
else:
    print('Por isso ele NAO E PRIMO')
