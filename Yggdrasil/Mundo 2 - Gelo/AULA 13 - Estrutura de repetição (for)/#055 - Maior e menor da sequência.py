min = 0
max = 0

for p in range(1, 6):
    peso = float(input(f'Qual peso da {p}ª pessoa? '))
    if p == 1:
        min = peso
        max = peso
    else:
        if peso > max:
            max = peso
        if peso < min:
            min = peso
print(f'O maior peso foi de {max}KG')
print(f'O menor peso foi de {min}KG')
