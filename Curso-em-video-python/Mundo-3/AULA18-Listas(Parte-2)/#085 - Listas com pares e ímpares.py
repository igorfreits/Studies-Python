numbers = [[], []]

for c in range(7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        numbers[0].append(n)
    else:
        numbers[1].append(n)

print(f'Números pares: \033[34m{numbers[0]}\033[m')
print(f'Números ímpares: \033[34m{numbers[1]}\033[m')
