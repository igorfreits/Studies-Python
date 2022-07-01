a = []
impares = []
pares = []
while True:
    n = int(input('Digite um numero: '))
    a.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    option = str(input('Deseja continuar? [S/N]')).upper().strip()
    if option == 'S':
        continue
    elif option == 'N':
        break
    else:
        print('Invalid option')

print(f'A lista completa é: {a}')
print(f'A lista de pares é: {pares}')
print(f'A lista de impares é {impares}')
